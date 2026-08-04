from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main layout
        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15
        )

        # App title
        title = Label(
            text='FeeTrack Academy',
            font_size=28,
            bold=True,
            size_hint=(1, 0.2)
        )

        # Developer name
        developer = Label(
            text='Developer: Joseph Mbui',
            font_size=16,
            size_hint=(1, 0.1)
        )

        # Dashboard heading
        heading = Label(
            text='Dashboard',
            font_size=24,
            bold=True,
            size_hint=(1, 0.15)
        )

        # Buttons
        btn_add = Button(
            text='Add Student',
            size_hint=(1, 0.15),
            background_color=(0, 0.4, 0.8, 1)
        )

        btn_list = Button(
            text='Student List',
            size_hint=(1, 0.15),
            background_color=(0, 0.4, 0.8, 1)
        )

        btn_payment = Button(
            text='Payments',
            size_hint=(1, 0.15),
            background_color=(0, 0.4, 0.8, 1)
        )

        btn_detail = Button(
            text='Student Details',
            size_hint=(1, 0.15),
            background_color=(0, 0.4, 0.8, 1)
        )

        btn_logout = Button(
            text='Logout',
            size_hint=(1, 0.15),
            background_color=(0.8, 0, 0, 1)
        )

        # Navigation
        btn_add.bind(on_press=lambda x: self.go_to('add_student'))
        btn_list.bind(on_press=lambda x: self.go_to('student_list'))
        btn_payment.bind(on_press=lambda x: self.go_to('payment'))
        btn_detail.bind(on_press=lambda x: self.go_to('student_detail'))
        btn_logout.bind(on_press=lambda x: self.go_to('login'))

        # Add widgets
        layout.add_widget(title)
        layout.add_widget(developer)
        layout.add_widget(heading)
        layout.add_widget(btn_add)
        layout.add_widget(btn_list)
        layout.add_widget(btn_payment)
        layout.add_widget(btn_detail)
        layout.add_widget(btn_logout)

        self.add_widget(layout)

    def go_to(self, screen_name):
        self.manager.current = screen_name
