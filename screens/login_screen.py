from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        title = Label(
            text='FeeTrack Academy Login',
            font_size=24,
            size_hint=(1, 0.2)
        )

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
            size_hint=(1, 0.2)
        )
        login_btn.bind(on_press=self.login)

        self.message = Label(
            text='',
            color=(1, 0, 0, 1),
            size_hint=(1, 0.2)
        )

        layout.add_widget(title)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(self.message)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username.text.strip()
        password = self.password.text.strip()

        if username == 'admin' and password == '1234':
            self.manager.current = 'dashboard'
        else:
            self.message.text = 'Invalid username or password'
