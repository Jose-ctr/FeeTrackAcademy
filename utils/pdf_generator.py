import os
from datetime import datetime

def generate_statement(student_name, total_fee, paid, filename):
    balance = total_fee - paid
    date_today = datetime.now().strftime("%Y-%m-%d")

    # PDF disabled for Android build test - using TXT instead
    # This avoids reportlab crash on Android
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"FeeTrack Academy\n")
        f.write(f"===========================\n")
        f.write(f"Date: {date_today}\n")
        f.write(f"Student: {student_name}\n")
        f.write(f"Total Fee: KES {total_fee:.2f}\n")
        f.write(f"Amount Paid: KES {paid:.2f}\n")
        f.write(f"Balance: KES {balance:.2f}\n")
        f.write(f"===========================\n")
        f.write(f"Developed by Joseph Mbui\n")

    return filename
