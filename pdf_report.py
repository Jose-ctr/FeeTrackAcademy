def generate_statement(student_name, total_fee, paid, filename):
    balance = total_fee - paid
    
    # PDF disabled for Android build test
    with open(filename, "w") as f:
        f.write(f"FeeTrack Academy\n")
        f.write(f"Student: {student_name}\n")
        f.write(f"Total Fee: KES {total_fee:.2f}\n")
        f.write(f"Amount Paid: KES {paid:.2f}\n")
        f.write(f"Balance: KES {balance:.2f}\n")
        f.write(f"Developed by Joseph Mbui\n")
    
    return filename
