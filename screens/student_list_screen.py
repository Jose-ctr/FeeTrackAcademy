from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class StudentListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Student List', font_size=24))

        layout.add_widget(Label(text='No students added yet'))

        back_btn = Button(text='Back')
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))

        layout.add_widget(back_btn)

        self.add_widget(layout)
