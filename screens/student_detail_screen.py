from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class StudentDetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Student Details', font_size=24))
        layout.add_widget(Label(text='Name: -'))
        layout.add_widget(Label(text='Class: -'))
        layout.add_widget(Label(text='Balance: -'))

        back_btn = Button(text='Back')
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'student_list'))

        layout.add_widget(back_btn)

        self.add_widget(layout)
