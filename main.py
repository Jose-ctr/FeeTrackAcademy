from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

import database


def show_message(title, message):
    popup = Popup(
        title=title,
        content=Label(text=message),
        size_hint=(0.8, 0.4)
    )
    popup.open()


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)

        layout.add_widget(Label(
            text='FeeTrack Academy',
            font_size='28sp',
            bold=True,
            color=(0, 0.3, 0.8, 1)
        ))

        layout.add_widget(Label(text='Login', font_size='22sp'))

        self.username = TextInput(
            hint_text='Username',
            multiline=False,
            size_hint_y=None,
            height='45dp'
        )

        self.password = TextInput(
            hint_text='Password',
            password=True,
            multiline=False,
            size_hint_y=None,
            height='45dp'
        )

        login_btn = Button(
            text='Login',
            size_hint_y=None,
            height='50dp',
            background_color=(0, 0.4, 0.9, 1)
        )
        login_btn.bind(on_press=self.login)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)

        layout.add_widget(Label(
            text='Developed by Joseph Mbui',
            size_hint_y=None,
            height='30dp'
        ))

        self.add_widget(layout)

    def login(self, instance):
        if self.username.text == 'admin' and self.password.text == '1234':
            self.manager.current = 'dashboard'
            self.username.text = ''
            self.password.text = ''
        else:
            show_message('Login Failed', 'Invalid username or password')


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        layout.add_widget(Label(
            text='Dashboard',
            font_size='26sp',
            bold=True,
            color=(0, 0.3, 0.8, 1)
        ))

        btn_add = Button(text='Add Student', size_hint_y=None, height='50dp')
        btn_view = Button(text='View Students', size_hint_y=None, height='50dp')
        btn_pay = Button(text='Record Payment', size_hint_y=None, height='50dp')
        btn_logout = Button(
            text='Logout',
            size_hint_y=None,
            height='50dp',
            background_color=(0.8, 0.2, 0.2, 1)
        )

        btn_add.bind(on_press=lambda x: setattr(self.manager, 'current', 'add_student'))
        btn_view.bind(on_press=lambda x: setattr(self.manager, 'current', 'view_students'))
        btn_pay.bind(on_press=lambda x: setattr(self.manager, 'current', 'payment'))
        btn_logout.bind(on_press=lambda x: setattr(self.manager, 'current', 'login'))

        layout.add_widget(btn_add)
        layout.add_widget(btn_view)
        layout.add_widget(btn_pay)
        layout.add_widget(btn_logout)

        layout.add_widget(Label(
            text='Developed by Joseph Mbui',
            size_hint_y=None,
            height='30dp'
        ))

        self.add_widget(layout)


class AddStudentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Add Student', font_size='24sp', bold=True))

        self.name_input = TextInput(hint_text='Student Name', multiline=False)
        self.phone_input = TextInput(hint_text='Phone Number', multiline=False)
        self.fee_input = TextInput(hint_text='Total Fee', multiline=False, input_filter='float')

        save_btn = Button(text='Save Student', size_hint_y=None, height='50dp')
        save_btn.bind(on_press=self.save_student)

        back_btn = Button(text='Back', size_hint_y=None, height='50dp')
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))

        layout.add_widget(self.name_input)
        layout.add_widget(self.phone_input)
        layout.add_widget(self.fee_input)
        layout.add_widget(save_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def save_student(self, instance):
        name = self.name_input.text.strip()
        phone = self.phone_input.text.strip()
        fee = self.fee_input.text.strip()

        if not name or not fee:
            show_message('Error', 'Name and fee are required')
            return

        database.add_student(name, phone, float(fee))

        self.name_input.text = ''
        self.phone_input.text = ''
        self.fee_input.text = ''

        show_message('Success', 'Student added successfully')


class ViewStudentsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        root.add_widget(Label(text='Students', font_size='24sp', bold=True))

        self.grid = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        scroll = ScrollView()
        scroll.add_widget(self.grid)

        refresh_btn = Button(text='Refresh', size_hint_y=None, height='50dp')
        refresh_btn.bind(on_press=self.load_students)

        back_btn = Button(text='Back', size_hint_y=None, height='50dp')
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))

        root.add_widget(scroll)
        root.add_widget(refresh_btn)
        root.add_widget(back_btn)

        self.add_widget(root)

    def on_pre_enter(self):
        self.load_students()

    def load_students(self, *args):
        self.grid.clear_widgets()

        students = database.get_students()

        if not students:
            self.grid.add_widget(Label(text='No students found', size_hint_y=None, height='40dp'))
            return

        for s in students:
            sid, name, phone, total_fee, paid = s
            balance = total_fee - paid

            text = (
                f'ID: {sid}\n'
                f'Name: {name}\n'
                f'Phone: {phone}\n'
                f'Total Fee: KES {total_fee:.2f}\n'
                f'Paid: KES {paid:.2f}\n'
                f'Balance: KES {balance:.2f}'
            )

            lbl = Label(
                text=text,
                size_hint_y=None,
                height='140dp',
                halign='left',
                valign='middle'
            )
            lbl.bind(size=lambda inst, val: setattr(inst, 'text_size', val))

            self.grid.add_widget(lbl)


class PaymentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Record Payment', font_size='24sp', bold=True))

        self.id_input = TextInput(hint_text='Student ID', multiline=False, input_filter='int')
        self.amount_input = TextInput(hint_text='Amount', multiline=False, input_filter='float')

        save_btn = Button(text='Save Payment', size_hint_y=None, height='50dp')
        save_btn.bind(on_press=self.save_payment)

        back_btn = Button(text='Back', size_hint_y=None, height='50dp')
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))

        layout.add_widget(self.id_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(save_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def save_payment(self, instance):
        sid = self.id_input.text.strip()
        amount = self.amount_input.text.strip()

        if not sid or not amount:
            show_message('Error', 'Enter student ID and amount')
            return

        database.record_payment(int(sid), float(amount))

        self.id_input.text = ''
        self.amount_input.text = ''

        show_message('Success', 'Payment recorded successfully')


class FeeTrackApp(App):
    def build(self):
        database.create_tables()

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(AddStudentScreen(name='add_student'))
        sm.add_widget(ViewStudentsScreen(name='view_students'))
        sm.add_widget(PaymentScreen(name='payment'))

        return sm


if __name__ == '__main__':
    FeeTrackApp().run()
