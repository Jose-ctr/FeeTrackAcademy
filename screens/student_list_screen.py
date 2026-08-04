from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class StudentListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        # Title
        layout.add_widget(
            Label(
                text='Student List',
                font_size=24,
                size_hint=(1, 0.1)
            )
        )

        # Temporary message
        layout.add_widget(
            Label(
                text='No students yet',
                font_size=18
            )
        )

        # Back button
        back_btn = Button(
            text='Back',
            size_hint=(1, 0.1)
        )

        back_btn.bind(
            on_press=lambda x: setattr(self.manager, 'current', 'dashboard')
        )

        layout.add_widget(back_btn)

        # Add layout to screen
        self.add_widget(layout)
