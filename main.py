from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login_screen import LoginScreen
from screens.dashboard_screen import DashboardScreen
from screens.add_student_screen import AddStudentScreen
from screens.student_list_screen import StudentListScreen
from screens.student_detail_screen import StudentDetailScreen
from screens.payment_screen import PaymentScreen


class FeeTrackApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(AddStudentScreen(name='add_student'))
        sm.add_widget(StudentListScreen(name='student_list'))
        sm.add_widget(StudentDetailScreen(name='student_detail'))
        sm.add_widget(PaymentScreen(name='payment'))

        return sm


if __name__ == '__main__':
    FeeTrackApp().run()
