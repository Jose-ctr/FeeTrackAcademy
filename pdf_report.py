from fpdf import FPDF

def generate_statement(student_name, total_fee, paid, filename='statement.pdf'):
    balance = total_fee - paid

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, 10, 'FeeTrack Academy', ln=True, align='C')
    pdf.ln(5)

    pdf.set_font('Arial', size=12)
    pdf.cell(0, 10, f'Student: {student_name}', ln=True)
    pdf.cell(0, 10, f'Total Fee: KES {total_fee:.2f}', ln=True)
    pdf.cell(0, 10, f'Amount Paid: KES {paid:.2f}', ln=True)
    pdf.cell(0, 10, f'Balance: KES {balance:.2f}', ln=True)
    pdf.ln(10)
    pdf.cell(0, 10, 'Developed by Joseph Mbui', ln=True, align='C')

    pdf.output(filename)
    return filename
