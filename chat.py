import os
import kivy

from kivy.app import App
from kivy.uix.label import Label             # Uix element that will hold text
from kivy.uix.gridlayout import GridLayout   # One of many layout structures
from kivy.uix.textinput import TextInput     # Allow for ...text input.
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

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

        # Added Join Button.
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())              # Just Take up the Empty column on the left
        self.add_widget(self.join)

    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        # Saving textfield details to a .txt file for autofill(convenient)
        with open("prev_details.txt", 'w') as prev_details:
            prev_details.write(f"{ip},{port},{username}")

        #print(f"Joining {ip}:{port} as {username}")

        info = f"Joining {ip}:{port} as {username}"
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = 'Info'


class ChatApp(App):
    def build(self):

        # Using screen manager to add multiple screens and navigate between them.
        self.screen_manager = ScreenManager()

        # We will use a passed in named to activate the Initial Connection Screen
        # 1 - Create a page
        # 2 - Create the new Screen
        # 3 - Add page to screen then add screen to screen manager
        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        # Information Page
        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Only one column
        self.cols = 1

        # One Label with a bigger font and a centered text
        self.message = Label(halign='center', valign='middle', font_size=32)

        # By default every widget returns it's side as [100, 100], it gets finally resized,
        # but we have to listen for size change to get a new one
        # more: https://github.com/kivy/kivy/issues/1044 ...
        self.message.bind(width=self.update_text_width)

        # Adding text widget to the layout
        self.add_widget(self.message)

    # Called with a message to update the message text in widget.
    def update_info(self, message):
        self.message.text = message

    # Called on Label width update, so we can set text width properly - to 90% of label width
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)

if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.run()
