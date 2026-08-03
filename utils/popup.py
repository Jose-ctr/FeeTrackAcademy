from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def show_popup(title, message):
    layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    layout.add_widget(Label(text=message))
    btn = Button(text='OK', size_hint_y=0.3)
    layout.add_widget(btn)
    popup = Popup(title=title, content=layout, size_hint=(0.8, 0.4))
    btn.bind(on_press=popup.dismiss)
    popup.open()
