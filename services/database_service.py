"""
Database service for FeeTrackAcademy.

Improvements:
- Use context managers for connections/cursors.
- Use sqlite3.Row for dict-like row access.
- Add payments table to record each payment (audit trail).
- Add typed methods: get_student, get_students, add_student, update/delete, record_payment, get_payments_for_student.
- PRAGMA tuning: foreign_keys=ON, journal_mode=WAL.
- Input validation and logging.
"""

from __future__ import annotations
import logging
import os
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

# Default DB path: environment variable FEE_DB or project root feetrack.db
DEFAULT_DB_PATH = Path(os.getenv(
    "FEE_DB",
    Path(__file__).resolve().parents[1] / "feetrack.db"
)).resolve()


class StudentNotFoundError(Exception):
    pass


class DatabaseService:
    DB_PATH: Path = DEFAULT_DB_PATH

    @classmethod
    def connect(cls) -> sqlite3.Connection:
        """
        Return a new sqlite3.Connection configured with sensible defaults.
        Callers should use context managers (with DatabaseService.connect() as conn: ...).
        """
        conn = sqlite3.connect(str(cls.DB_PATH), detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        # PRAGMA settings
        conn.execute("PRAGMA foreign_keys = ON")
        # WAL improves concurrency for many readers / single writer
        try:
            conn.execute("PRAGMA journal_mode=WAL")
        except sqlite3.DatabaseError:
            # Not fatal — continue with default
            logger.debug("Unable to set journal_mode=WAL; continuing with default.")
        return conn

    @classmethod
    def create_tables(cls) -> None:
        """Create students and payments tables if they don't exist."""
        with cls.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT,
                    total_fee REAL DEFAULT 0,
                    paid REAL DEFAULT 0
                )
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
                    amount REAL NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()
        logger.info("Database tables ensured at %s", cls.DB_PATH)

    @classmethod
    def add_student(cls, name: str, phone: Optional[str], total_fee: float = 0.0) -> int:
        """
        Insert a new student. Returns the new student's id.
        """
        if not name:
            raise ValueError("name is required")
        if total_fee < 0:
            raise ValueError("total_fee cannot be negative")

        with cls.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO students (name, phone, total_fee, paid) VALUES (?, ?, ?, 0)",
                (name, phone, float(total_fee)),
            )
            student_id = cur.lastrowid
            conn.commit()
        logger.info("Added student %s (id=%s)", name, student_id)
        return student_id

    @classmethod
    def get_students(cls, limit: Optional[int] = None) -> List[Dict]:
        """Return all students as list of dicts, newest first by id."""
        query = "SELECT * FROM students ORDER BY id DESC"
        if limit is not None:
            query += " LIMIT ?"
            params = (limit,)
        else:
            params = ()
        with cls.connect() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = [dict(r) for r in cur.fetchall()]
        return rows

    @classmethod
    def get_student(cls, student_id: int) -> Optional[Dict]:
        """Return a single student dict or None if not found."""
        with cls.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            row = cur.fetchone()
        return dict(row) if row else None

    @classmethod
    def update_student(
        cls,
        student_id: int,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        total_fee: Optional[float] = None,
    ) -> None:
        """Update provided fields for a student."""
        if total_fee is not None and total_fee < 0:
            raise ValueError("total_fee cannot be negative")

        fields = []
        params = []
        if name is not None:
            fields.append("name = ?")
            params.append(name)
        if phone is not None:
            fields.append("phone = ?")
            params.append(phone)
        if total_fee is not None:
            fields.append("total_fee = ?")
            params.append(float(total_fee))

        if not fields:
            return  # nothing to do

        params.append(student_id)
        sql = f"UPDATE students SET {', '.join(fields)} WHERE id = ?"

        with cls.connect() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            if cur.rowcount == 0:
                raise StudentNotFoundError(f"Student id={student_id} not found")
            conn.commit()
        logger.info("Updated student id=%s", student_id)

    @classmethod
    def record_payment(cls, student_id: int, amount: float) -> int:
        """
        Record a payment for a student.
        Adds a row to payments and updates students.paid atomically.
        Returns the payment id.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive")

        with cls.connect() as conn:
            cur = conn.cursor()
            # ensure student exists
            cur.execute("SELECT total_fee, paid FROM students WHERE id = ?", (student_id,))
            row = cur.fetchone()
            if not row:
                raise StudentNotFoundError(f"Student id={student_id} not found")

            total_fee = float(row["total_fee"] or 0.0)
            current_paid = float(row["paid"] or 0.0)
            new_paid = current_paid + float(amount)
            if total_fee and new_paid > total_fee:
                # allow overpayment only if desired; here we block by default
                raise ValueError("Payment would exceed total fee; adjust amount or update total_fee first")

            # Insert payment audit record
            cur.execute(
                "INSERT INTO payments (student_id, amount, created_at) VALUES (?, ?, ?)",
                (student_id, float(amount), datetime.utcnow()),
            )
            payment_id = cur.lastrowid
            # Update student paid total
            cur.execute(
                "UPDATE students SET paid = paid + ? WHERE id = ?",
                (float(amount), student_id),
            )
            conn.commit()
        logger.info("Recorded payment id=%s for student id=%s amount=%s", payment_id, student_id, amount)
        return payment_id

    @classmethod
    def get_payments_for_student(cls, student_id: int, limit: Optional[int] = None) -> List[Dict]:
        """Return payments for a student ordered by newest first."""
        query = "SELECT * FROM payments WHERE student_id = ? ORDER BY id DESC"
        params = [student_id]
        if limit is not None:
            query += " LIMIT ?"
            params.append(limit)
        with cls.connect() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = [dict(r) for r in cur.fetchall()]
        return rows

    @classmethod
    def delete_student(cls, student_id: int) -> None:
        """Delete a student and cascade-delete payments (if any)."""
        with cls.connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
            if cur.rowcount == 0:
                raise StudentNotFoundError(f"Student id={student_id} not found")
            conn.commit()
        logger.info("Deleted student id=%s", student_id)
