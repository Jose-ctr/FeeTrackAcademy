import sqlite3

DB_NAME = "feetrack.db"

class DatabaseService:

    @staticmethod
    def connect():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def create_tables():
        conn = DatabaseService.connect()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            total_fee REAL DEFAULT 0,
            paid REAL DEFAULT 0
        )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def add_student(name, phone, total_fee):
        conn = DatabaseService.connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students(name, phone, total_fee, paid) VALUES(?,?,?,0)",
            (name, phone, total_fee)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_students():
        conn = DatabaseService.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students ORDER BY id DESC")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def record_payment(student_id, amount):
        conn = DatabaseService.connect()
        cur = conn.cursor()
        cur.execute(
            "UPDATE students SET paid = paid + ? WHERE id=?",
            (amount, student_id)
        )
        conn.commit()
        conn.close()
