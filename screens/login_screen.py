from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from utils.popup import show_popup


class LoginScreen(Screen):
    """
    Simple login screen for FeeTrack Academy.

    Replace the dummy authentication in `on_login` with real auth (API, Firebase, etc.).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        layout.add_widget(Label(text="Please sign in", size_hint=(1, 0.2)))

        self.username = TextInput(hint_text="Username", multiline=False, size_hint=(1, 0.15))
        layout.add_widget(self.username)

        self.password = TextInput(hint_text="Password", password=True, multiline=False, size_hint=(1, 0.15))
        layout.add_widget(self.password)

        login_btn = Button(text="Login", size_hint=(1, 0.18))
        login_btn.bind(on_release=self.on_login)
        layout.add_widget(login_btn)

        self.add_widget(layout)

    def on_login(self, instance):
        user = (self.username.text or "").strip()
        pwd = (self.password.text or "").strip()

        if not user or not pwd:
            # show_popup(title, message)
            show_popup("Error", "Please enter username and password")
            return

        # TODO: replace this with real authentication logic
        if user == "admin" and pwd == "password":
            show_popup("Success", "Logged in")
            # Example navigation (uncomment and adapt if you have a Home screen):
            # if self.manager:
            #     self.manager.current = "home_screen"
        else:
            show_popup("Error", "Invalid credentials")
