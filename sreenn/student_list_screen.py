from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from services.database_service import DatabaseService


class StudentListScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        root.add_widget(Label(
            text='Student List',
            font_size='24sp',
            bold=True
        ))

        self.grid = GridLayout(
            cols=1,
            spacing=8,
            size_hint_y=None
        )

        self.grid.bind(minimum_height=self.grid.setter('height'))

        scroll = ScrollView()
        scroll.add_widget(self.grid)

        refresh_btn = Button(
            text='Refresh',
            size_hint_y=None,
            height='50dp'
        )

        refresh_btn.bind(on_press=self.load_students)

        back_btn = Button(
            text='Back',
            size_hint_y=None,
            height='50dp'
        )

        back_btn.bind(
            on_press=lambda x: setattr(self.manager, 'current', 'dashboard')
        )

        root.add_widget(scroll)
        root.add_widget(refresh_btn)
        root.add_widget(back_btn)

        self.add_widget(root)

    def on_pre_enter(self):
        self.load_students()

    def load_students(self, *args):
        self.grid.clear_widgets()

        students = DatabaseService.get_students()

        if not students:
            self.grid.add_widget(Label(
                text='No students found',
                size_hint_y=None,
                height='40dp'
            ))
            return

        for s in students:
            sid, name, phone, total_fee, paid = s
            balance = total_fee - paid

            text = (
                f'ID: {sid}\\n'
                f'Name: {name}\\n'
                f'Phone: {phone}\\n'
                f'Total Fee: KES {total_fee:.2f}\\n'
                f'Paid: KES {paid:.2f}\\n'
                f'Balance: KES {balance:.2f}'
            )

            lbl = Label(
                text=text,
                size_hint_y=None,
                height='140dp',
                halign='left',
                valign='middle'
            )

            lbl.bind(
                size=lambda inst, val: setattr(inst, 'text_size', val)
            )

            self.grid.add_widget(lbl)
