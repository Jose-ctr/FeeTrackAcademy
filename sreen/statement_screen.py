from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from utils.popup import show_popup


class StatementScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        layout.add_widget(Label(
            text='Generate Statement',
            font_size='24sp',
            bold=True
        ))

        self.id_input = TextInput(
            hint_text='Student ID',
            multiline=False,
            input_filter='int'
        )

        generate_btn = Button(
            text='Generate Statement',
            size_hint_y=None,
            height='50dp'
        )

        generate_btn.bind(on_press=self.generate_statement)

        back_btn = Button(
            text='Back',
            size_hint_y=None,
            height='50dp'
        )

        back_btn.bind(
            on_press=lambda x: setattr(self.manager, 'current', 'dashboard')
        )

        layout.add_widget(self.id_input)
        layout.add_widget(generate_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def generate_statement(self, instance):
        sid = self.id_input.text.strip()

        if not sid:
            show_popup('Error', 'Enter student ID')
            return

        show_popup(
            'Statement',
            f'Statement generated for Student ID {sid}'
        )
