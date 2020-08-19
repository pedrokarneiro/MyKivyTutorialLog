# Events and Instance Variables
# Implements a manual counter. Each time the button is pressed, on release, the
# label will be incremented by 1.
# Date created: 2020-07-18
# \EstudoKivy\HelloWorldKivy\02_Events_And_Instance_Variables.py
# Pedro Carneiro Junior - pedrokarneiro.bsa@gmail.com
# NOTES: Will not run with F5 from within IDLE,
# ------ Will run only by "<file_name>.py" command in command line.
#################################################################################

from kivy.app import App                 # This is the app itself.
from kivy.uix.button import Button       # This is the button class.
from kivy.uix.boxlayout import BoxLayout # This is the box layout class (a container that arranges the items within it in the layout like boxes).
from kivy.uix.label import Label         # This is a label class to show text.

class Test(App):                         # This class inherits from App.
    def build(self):                     # This is the constructor that shows the button in the app.
        box = BoxLayout(orientation='vertical') # This is the outter box (will be shown at the end with everything within it).
        # These objects will go in the box.
        button = Button(text = 'Click me to count', font_size=30, on_release=self.incrementar) # self.incrementar is called on the release of the click on the button.
        self.label = Label(text='1', font_size=30) # self.label because this label is the instance variable of this object instance.
        # This method is the one that adds the button and lebal widgets to the box.
        box.add_widget(button)
        box.add_widget(self.label)
        # This will show the outter box (and all within it) by returning it.
        return box
    
    def incrementar(self, button):
        # The instance variable self.label here gets its text property incremented by 1.
        self.label.text = str(int(self.label.text)+1)

Test().run()                       # This calls the run method of the Test class.
