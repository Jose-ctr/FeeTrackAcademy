import sqlite3

DB_NAME = 'feetrack.db'

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        total_fee REAL DEFAULT 0,
        paid REAL DEFAULT 0
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        amount REAL,
        date TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    ''')

    conn.commit()
    conn.close()

def add_student(name, phone, total_fee):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO students(name, phone, total_fee, paid) VALUES(?,?,?,0)',
        (name, phone, total_fee)
    )
    conn.commit()
    conn.close()

def get_students():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT id, name, phone, total_fee, paid, (total_fee - paid) as balance FROM students')
    rows = cur.fetchall()
    conn.close()
    return rows

def record_payment(student_id, amount):
    conn = connect()
    cur = conn.cursor()
    cur.execute('UPDATE students SET paid = paid + ? WHERE id=?', (amount, student_id))
    cur.execute('INSERT INTO payments(student_id, amount) VALUES(?,?)', (student_id, amount))
    conn.commit()
    conn.close()

def get_student_payments(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM payments WHERE student_id=? ORDER BY date DESC', (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

create_tables()
