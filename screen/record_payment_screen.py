from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from services.database_service import DatabaseService
from utils.popup import show_popup


class RecordPaymentScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        self.id_input = TextInput(
            hint_text='Student ID',
            multiline=False,
            input_filter='int'
        )

        self.amount_input = TextInput(
            hint_text='Amount Paid',
            multiline=False,
            input_filter='float'
        )

        save_btn = Button(
            text='Record Payment',
            size_hint_y=None,
            height='50dp'
        )

        save_btn.bind(on_press=self.record_payment)

        back_btn = Button(
            text='Back',
            size_hint_y=None,
            height='50dp'
        )

        back_btn.bind(
            on_press=lambda x: setattr(self.manager, 'current', 'dashboard')
        )

        layout.add_widget(self.id_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(save_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def record_payment(self, instance):
        sid = self.id_input.text.strip()
        amount = self.amount_input.text.strip()

        if not sid or not amount:
            show_popup('Error', 'Enter student ID and amount')
            return

        DatabaseService.record_payment(int(sid), float(amount))

        self.id_input.text = ''
        self.amount_input.text = ''

        show_popup('Success', 'Payment recorded successfully')
