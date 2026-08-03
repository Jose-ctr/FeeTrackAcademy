import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

DB_NAME = 'feetrack.db'


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            admission_no TEXT,
            fee_paid REAL,
            balance REAL
        )
    ''')

    conn.commit()
    conn.close()


class FeeTrackApp(App):

    def build(self):
        init_db()

        root = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        # Title
        title = Label(
            text='FeeTrack Academy',
            font_size='24sp',
            size_hint_y=None,
            height=50
        )
        root.add_widget(title)

        # Input fields
        self.name_input = TextInput(
            hint_text='Student Name',
            multiline=False,
            size_hint_y=None,
            height=45
        )

        self.adm_input = TextInput(
            hint_text='Admission Number',
            multiline=False,
            size_hint_y=None,
            height=45
        )

        self.paid_input = TextInput(
            hint_text='Fee Paid (KES)',
            multiline=False,
            size_hint_y=None,
            height=45
        )

        self.balance_input = TextInput(
            hint_text='Balance (KES)',
            multiline=False,
            size_hint_y=None,
            height=45
        )

        root.add_widget(self.name_input)
        root.add_widget(self.adm_input)
        root.add_widget(self.paid_input)
        root.add_widget(self.balance_input)

        # Save button
        save_btn = Button(
            text='Save Student',
            size_hint_y=None,
            height=50
        )
        save_btn.bind(on_press=self.save_student)
        root.add_widget(save_btn)

        # Refresh button
        refresh_btn = Button(
            text='Refresh List',
            size_hint_y=None,
            height=50
        )
        refresh_btn.bind(on_press=self.load_students)
        root.add_widget(refresh_btn)

        # Student list area
        self.grid = GridLayout(
            cols=1,
            spacing=5,
            size_hint_y=None
        )
        self.grid.bind(minimum_height=self.grid.setter('height'))

        scroll = ScrollView()
        scroll.add_widget(self.grid)

        root.add_widget(scroll)

        # Load saved students
        self.load_students()

        return root

    def save_student(self, instance):
        name = self.name_input.text.strip()
        adm = self.adm_input.text.strip()

        try:
            paid = float(self.paid_input.text)
        except:
            paid = 0.0

        try:
            balance = float(self.balance_input.text)
        except:
            balance = 0.0

        if name == '' or adm == '':
            return

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        c.execute(
            'INSERT INTO students(name, admission_no, fee_paid, balance) VALUES (?, ?, ?, ?)',
            (name, adm, paid, balance)
        )

        conn.commit()
        conn.close()

        # Clear inputs
        self.name_input.text = ''
        self.adm_input.text = ''
        self.paid_input.text = ''
        self.balance_input.text = ''

        # Reload list
        self.load_students()

    def load_students(self, instance=None):
        self.grid.clear_widgets()

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        c.execute(
            'SELECT name, admission_no, fee_paid, balance FROM students ORDER BY id DESC'
        )

        rows = c.fetchall()
        conn.close()

        if not rows:
            self.grid.add_widget(
                Label(
                    text='No students saved yet.',
                    size_hint_y=None,
                    height=40
                )
            )
            return

        for name, adm, paid, balance in rows:
            text = (
                f'{name} | Adm: {adm} | '
                f'Paid: KES {paid:.2f} | '
                f'Balance: KES {balance:.2f}'
            )

            lbl = Label(
                text=text,
                size_hint_y=None,
                height=40,
                halign='left',
                valign='middle'
            )

            lbl.bind(size=lambda s, v: setattr(s, 'text_size', v))
            self.grid.add_widget(lbl)


if __name__ == '__main__':
    FeeTrackApp().run()

# Developed by Joseph Mbui
