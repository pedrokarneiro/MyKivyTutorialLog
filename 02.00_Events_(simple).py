# Simple event handling.
# Date created: 2020-07-18
# \EstudoKivy\HelloWorldKivy\02_Events_(simple).py
# Pedro Carneiro Junior - pedrokarneiro.bsa@gmail.com
# NOTES: Will not run with F5 from within IDLE,
# ------ Will run only by "python <file_name>.py" command in command line.
#################################################################################

from kivy.app import App                 # This is the app itself.
from kivy.uix.button import Button       # This is the button class.
from kivy.uix.boxlayout import BoxLayout # This is the box layout class (a container that arranges the items within it in the layout like boxes).

class Test(App):                         # This class inherits from App.
    def build(self):                     # This is the constructor that shows the button in the app.
        box = BoxLayout(orientation='vertical') # This is the outter box (will be shown at the end with everything within it).
        # These objects will go in the box.
        button = Button(text = 'Button 1', font_size=30, on_release=self.incrementar)
        # This method is the one that adds the button and lebal widgets to the box.
        box.add_widget(button)
        # This will show the outter box (and all within it) by returning it.
        return box
    
    def incrementar(self, button):
        button.text = 'Soltei'

Test().run()                       # This calls the run method of the Test class.
