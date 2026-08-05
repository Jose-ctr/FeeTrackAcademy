from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from utils.popup import show_popup


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "login"

        # Light background color
        Window.clearcolor = (0.95, 0.97, 1, 1)

        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=15
        )

        # App title
        title = Label(
            text='FeeTrack Academy',
            font_size='30sp',
            bold=True,
            size_hint_y=None,
            height='60dp',
            color=(0.1, 0.2, 0.5, 1)
        )

        # Subtitle
        subtitle = Label(
            text='School Fee Management System',
            font_size='18sp',
            size_hint_y=None,
            height='35dp',
            color=(0.2, 0.2, 0.2, 1)
        )

        # Developer credit
        developer = Label(
            text='Developed by Joseph Mbui',
            font_size='14sp',
            size_hint_y=None,
            height='30dp',
            color=(0.4, 0.4, 0.4, 1)
        )

        # Username input
        self.username = TextInput(
            hint_text='Username',
            multiline=False,
            size_hint_y=None,
            height='45dp',
            font_size='16sp'
        )

        # Password input
        self.password = TextInput(
            hint_text='Password',
            password=True,
            multiline=False,
            size_hint_y=None,
            height='45dp',
            font_size='16sp'
        )

        # Press Enter to login
        self.password.bind(on_text_validate=self._on_enter)

        # Login button
        self.login_btn = Button(
            text='Login',
            size_hint_y=None,
            height='50dp',
            font_size='18sp',
            background_normal='',
            background_color=(0.1, 0.4, 0.9, 1)
        )

        self.login_btn.bind(on_press=self.login)

        # Message label
        self.message = Label(
            text='',
            color=(1, 0, 0, 1),
            size_hint_y=None,
            height='30dp'
        )

        # Add widgets
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(developer)
        layout.add_widget(Label(size_hint_y=None, height='20dp'))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.login_btn)
        layout.add_widget(self.message)

        self.add_widget(layout)

        # Focus username when screen opens
        Clock.schedule_once(
            lambda dt: setattr(self.username, 'focus', True),
            0.2
        )

    def _on_enter(self, instance):
        self.login(self.login_btn)

    def set_message(self, text, color=(1, 0, 0, 1)):
        self.message.text = text
        self.message.color = color

    def login(self, instance):
        username = (self.username.text or '').strip()
        password = (self.password.text or '').strip()

        if not username or not password:
            self.set_message('Please enter username and password.')
            show_popup('Missing Information', 'Please enter both username and password.')
            return

        # Disable button briefly
        self.login_btn.disabled = True
        self.set_message('Logging in...', color=(0.1, 0.3, 0.8, 1))

        Clock.schedule_once(
            lambda dt, u=username, p=password: self._authenticate(u, p),
            0.1
        )

    def _authenticate(self, username, password):
        # Demo credentials
        if username == 'admin' and password == '1234':
            self.set_message('Login successful!', color=(0, 0.6, 0, 1))

            # Clear fields
            self.username.text = ''
            self.password.text = ''

            self.login_btn.disabled = False

            # Navigate to dashboard
            if self.manager:
                self.manager.current = 'dashboard'
        else:
            self.password.text = ''
            self.login_btn.disabled = False
            self.set_message('Invalid username or password')
            show_popup('Login Failed', 'Invalid username or password')
