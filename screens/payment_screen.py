from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class PaymentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Record Payment', font_size=24))

        self.amount_input = TextInput(hint_text='Amount Paid')

        layout.add_widget(self.amount_input)

        save_btn = Button(text='Save Payment')
        back_btn = Button(text='Back')

        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))

        layout.add_widget(save_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)
