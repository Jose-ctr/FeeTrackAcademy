from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        self.add_widget(Label(
            text='FeeTrack Academy',
            font_size='28sp',
            bold=True
        ))

        self.add_widget(Label(
            text='Developed by Joseph Mbui',
            font_size='16sp'
        ))

        self.add_widget(Label(
            text='School Fee Management System',
            font_size='20sp'
        ))

        self.add_widget(Label(
            text='APK Build Test Successful',
            font_size='18sp'
        ))

        btn = Button(
            text='Start',
            size_hint=(1, None),
            height=50
        )
        self.add_widget(btn)


class FeeTrackApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    FeeTrackApp().run()

---

"database.py"

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
    cur.execute('SELECT * FROM students')
    rows = cur.fetchall()
    conn.close()
    return rows


def record_payment(student_id, amount):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        'UPDATE students SET paid = paid + ? WHERE id=?',
        (amount, student_id)
    )
    conn.commit()
    conn.close()


create_tables()

---

"pdf_report.py"

def generate_statement(student_name, total_fee, paid, filename):
    balance = total_fee - paid

    # Temporary text statement for Android build test
    with open(filename, 'w') as f:
        f.write('FeeTrack Academy\\n')
        f.write(f'Student: {student_name}\\n')
        f.write(f'Total Fee: KES {total_fee:.2f}\\n')
        f.write(f'Amount Paid: KES {paid:.2f}\\n')
        f.write(f'Balance: KES {balance:.2f}\\n')
        f.write('Developed by Joseph Mbui\\n')

    return filename

---

"buildozer.spec"

[app]
title = FeeTrack Academy
package.name = feetrack
package.domain = com.josephmbui
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,xml
version = 1.0.0
version.code = 1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
author = Joseph Mbui
author.email = mbuijoseph51@gmail.com

# Android 11+
android.api = 33
android.minapi = 30
android.archs = arm64-v8a
android.permissions = INTERNET
android.accept_sdk_license = True

[buildozer]
log_level = 2

---

".github/workflows/android.yml"

Create folders ".github/workflows/" then create "android.yml".

name: Build Android APK

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04
    timeout-minutes: 240

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y --no-install-recommends \
            git zip unzip autoconf libtool pkg-config \
            zlib1g-dev libncurses5-dev libncursesw5-dev \
            cmake libffi-dev libssl-dev build-essential

      - name: Install Python packages
        run: |
          python -m pip install --upgrade pip setuptools wheel
          python -m pip install buildozer==1.5.0 cython==0.29.33 virtualenv

      - name: Setup Android SDK
        uses: android-actions/setup-android@v3

      - name: Check buildozer.spec exists
        run: |
          if [ ! -f buildozer.spec ]; then
            echo '::error::buildozer.spec not found in repo root'
            ls -la
            exit 1
          fi
          echo 'Found buildozer.spec'

      - name: Build APK
        run: |
          yes | buildozer -v android debug 2>&1 | tee buildozer-output.txt

      - name: Show build files
        if: always()
        run: |
          echo '=== bin directory ==='
          ls -lah bin || true

      - name: Upload APK
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: FeeTrack-APK
          path: bin/*.apk
          if-no-files-found: error

      - name: Upload Buildozer Log
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: buildozer-log
          path: buildozer-output.txt

---

"README.md"

# FeeTrack Academy

Android school fee management application.

**Developed by Joseph Mbui**

## Features
- Student registration
- Fee payment recording
- Balance calculation
- Android 11+ support
- Kivy mobile interface

Package: `com.josephmbui.feetrack`

---

How to execute

1. Create all files above in your GitHub repo.
2. Commit and push.
3. Open GitHub → Actions.
4. Click Build Android APK.
5. Click Run workflow.
6. Wait for Completed ✅.
7. Download FeeTrack-APK from Artifacts.
8. Extract the ZIP and install the APK on your Android phone.

This is a complete buildable project for your current stage. Once the APK installs successfully, I can help you add:

- Login screen ("admin / 1234")
- Add student form
- Record payment form
- Search students
- Real PDF receipts using "reportlab"
- Blue FA logo and professional dashboard 🔥📱.
