import os

import kivy
from kivy.app import App
from kivy.uix.label import Label             # Uix element that will hold text
from kivy.uix.gridlayout import GridLayout   # One of many layout structures
from kivy.uix.textinput import TextInput     # Allow for ...text input.
from kivy.uix.button import Button

kivy.require("1.10.1")

# An actual app normally consists of many different 'pages' or 'screens'.
# Inherit from GridLayout

class ConnectPage(GridLayout):

    # runs on init
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage and GridLayout
        super().__init__(**kwargs)

        self.cols = 2  # two columns for the grid

        # Reads settings from text file, or uses empty strings
        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt", "r") as file:
                formatted_file = file.read().split(",")
                prev_ip = formatted_file[0]
                prev_port = formatted_file[1]
                prev_username = formatted_file[2]
        else:
            prev_ip = ''
            prev_port = ''
            prev_username = ''


        # widgets added in order, since order matters.
        self.add_widget(Label(text='IP'))     # widget 1 added to top left
        self.ip = TextInput(text=prev_ip, multiline=False)  # Defining 'self-ip'
        self.add_widget(self.ip)              # widget 2 added to top right

        self.add_widget(Label(text='Port'))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='Username'))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())              # Just Take up the Empty column on the left
        self.add_widget(self.join)
        #self.join.bind(on_press=self.join_button)

    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        with open ("prev_details.txt", 'w') as prev_details:
            prev_details.write(f"{ip}, {port}, {username}")
            # Saving textfield details to a .txt file for autofill(convenient)

        # Joining 127.0.0.1:1234 as sentdex
        print(f"Joining {ip}:{port} as {username}")

class EpicApp(App):
    def build(self):
        return ConnectPage()



if __name__ == "__main__":
    EpicApp().run()
