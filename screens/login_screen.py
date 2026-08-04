from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.logger import Logger

import hashlib
import hmac


# -------------------------------
# Demo secure login configuration
# -------------------------------
_DEMO_SALT = b"fee-track-academy-demo-salt"
_DEMO_ADMIN_HASH = hashlib.pbkdf2_hmac(
    "sha256",
    b"1234",
    _DEMO_SALT,
    100_000
)

MAX_FAILED_ATTEMPTS = 5
LOCKOUT_SECONDS = 30


def authenticate(username: str, password: str) -> bool:
    """
    Demo authentication.
    Replace this with a real database or API authentication in production.
    """
    if not username or not password:
        return False

    if username != "admin":
        return False

    try:
        candidate = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            _DEMO_SALT,
            100_000
        )
        return hmac.compare_digest(candidate, _DEMO_ADMIN_HASH)
    except Exception as e:
        Logger.exception("Login authentication error: %s", e)
        return False


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "login"

        Window.clearcolor = (0.95, 0.95, 0.97, 1)

        self.failed_attempts = 0
        self.locked_until = 0

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        title = Label(
            text="FeeTrack Academy Login",
            font_size=24,
            size_hint=(1, 0.2)
        )

        self.username = TextInput(
            hint_text="Username",
            multiline=False,
            size_hint=(1, None),
            height=40
        )

        self.password = TextInput(
            hint_text="Password",
            password=True,
            multiline=False,
            size_hint=(1, None),
            height=40
        )

        # Press Enter to login
        self.password.bind(on_text_validate=self._on_enter)

        self.login_btn = Button(
            text="Login",
            size_hint=(1, None),
            height=48
        )
        self.login_btn.bind(on_release=self.login)

        self.message = Label(
            text="",
            color=(1, 0, 0, 1),
            size_hint=(1, 0.2)
        )

        layout.add_widget(title)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.login_btn)
        layout.add_widget(self.message)

        self.add_widget(layout)

        # Focus username field when screen opens
        Clock.schedule_once(
            lambda dt: setattr(self.username, "focus", True),
            0.1
        )

    def _on_enter(self, instance):
        self.login(self.login_btn)

    def _set_message(self, text, color=(1, 0, 0, 1)):
        self.message.text = text
        self.message.color = color

    def _start_lockout(self):
        self.locked_until = Clock.get_time() + LOCKOUT_SECONDS
        self._set_message(
            f"Too many failed attempts. Try again in {LOCKOUT_SECONDS} seconds."
        )
        self.login_btn.disabled = True
        Clock.schedule_once(self._unlock, LOCKOUT_SECONDS)

    def _unlock(self, dt):
        self.failed_attempts = 0
        self.locked_until = 0
        self.login_btn.disabled = False
        self._set_message("")

    def login(self, instance):
        now = Clock.get_time()

        if self.locked_until and now < self.locked_until:
            remaining = int(self.locked_until - now)
            self._set_message(f"Locked out. Try again in {remaining} seconds.")
            return

        username = (self.username.text or "").strip()
        password = (self.password.text or "").strip()

        if not username or not password:
            self._set_message("Please enter both username and password.")
            return

        self.login_btn.disabled = True
        self._set_message(
            "Logging in...",
            color=(0.2, 0.2, 0.8, 1)
        )

        Clock.schedule_once(
            lambda dt: self._do_authenticate(username, password),
            0.1
        )

    def _do_authenticate(self, username, password):
        try:
            success = authenticate(username, password)
        except Exception:
            success = False

        if success:
            Logger.info(
                "Login successful for user '%s'",
                username
            )

            self._set_message("", color=(0, 0, 0, 0))

            # Clear fields after successful login
            self.password.text = ""
            self.username.text = ""

            self.failed_attempts = 0
            self.login_btn.disabled = False

            if self.manager:
                self.manager.current = "dashboard"

        else:
            Logger.warning(
                "Login failed for user '%s'",
                username
            )

            self.failed_attempts += 1
            self.password.text = ""
            self._set_message("Invalid username or password")

            if self.failed_attempts >= MAX_FAILED_ATTEMPTS:
                self._start_lockout()
            else:
                self.login_btn.disabled = False
                
