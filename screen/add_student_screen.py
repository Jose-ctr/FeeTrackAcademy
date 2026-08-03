from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from services.database_service import DatabaseService
from utils.popup import show_popup


class AddStudentScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        self.name_input = TextInput(
            hint_text='Student Name',
            multiline=False
        )

        self.phone_input = TextInput(
            hint_text='Phone Number',
            multiline=False
        )

        self.fee_input = TextInput(
            hint_text='Total Fee',
            multiline=False,
            input_filter='float'
        )

        save_btn = Button(
            text='Save Student',
            size_hint_y=None,
            height='50dp'
        )

        save_btn.bind(on_press=self.save_student)

        back_btn = Button(
            text='Back',
            size_hint_y=None,
            height='50dp'
        )

        back_btn.bind(
            on_press=lambda x: setattr(self.manager, 'current', 'dashboard')
        )

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
            show_popup('Error', 'Name and fee are required')
            return

        DatabaseService.add_student(name, phone, float(fee))

        self.name_input.text = ''
        self.phone_input.text = ''
        self.fee_input.text = ''

        show_popup('Success', 'Student added successfully')
