import kivy
from kivy.app import App
from kivy.uix.label import Label  # Uix element that will hold text

from kivy.uix.gridlayout import GridLayout   # One of many layout structures
from kivy.uix.textinput import TextInput  # Allow for ...text input

kivy.require("1.10.1")

# An actual app normally consists of many different 'pages' or 'screens'.
# Inherit from GridLayout

class ConnectPage(GridLayout):

    # runs on init
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage and GridLayout
        super().__init__(**kwargs)

        self.cols = 2  # two columns for the grid

        # widgets added in order, since order matters.
        self.add_widget(Label(text='IP'))  # widget 1 added to top left
        self.ip = TextInput(multiline=False) # Defining 'self-ip'
        self.add_widget(self.ip)  # widget 2 added to top right

        self.add_widget(Label(text='Port'))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)


class EpicApp(App):
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    EpicApp().run()






