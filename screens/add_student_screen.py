from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class AddStudentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Add Student', font_size=24))

        self.name_input = TextInput(hint_text='Student Name')
        self.class_input = TextInput(hint_text='Class')

        layout.add_widget(self.name_input)
        layout.add_widget(self.class_input)

        save_btn = Button(text='Save Student')
        back_btn = Button(text='Back')

        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))

        layout.add_widget(save_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)
