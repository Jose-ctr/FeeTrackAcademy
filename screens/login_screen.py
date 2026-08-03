from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from utils.popup import show_popup


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=15
        )

        layout.add_widget(Label(
            text='FeeTrack Academy',
            font_size='28sp',
            bold=True
        ))

        layout.add_widget(Label(
            text='Developed by Joseph Mbui',
            font_size='16sp'
        ))

        self.username = TextInput(
            hint_text='Username',
            multiline=False
        )

        self.password = TextInput(
            hint_text='Password',
            password=True,
            multiline=False
        )

        login_btn = Button(
            text='Login',
            size_hint_y=None,
            height='50dp'
        )

        login_btn.bind(on_press=self.login)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)

        self.add_widget(layout)

    def login(self, instance):
        if self.username.text == 'admin' and self.password.text == '1234':
            self.manager.current = 'dashboard'
        else:
            show_popup('Login Failed', 'Invalid username or password')
