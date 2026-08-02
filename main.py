from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        self.add_widget(Label(text='FeeTrack Academy', font_size=28))
        self.add_widget(Label(text='Developed by Joseph Mbui', font_size=16))
        self.add_widget(Label(text='Welcome to FeeTrack Academy', font_size=20))

        btn = Button(text='Start', size_hint=(1, None), height=50)
        self.add_widget(btn)

class FeeTrackApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    FeeTrackApp().run()
