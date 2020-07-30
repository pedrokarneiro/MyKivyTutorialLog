# Hello World, simple Kivy app
# Date created: 2020-07-2020
# \EstudoKivy\HelloWorldKivy\main.py
# Pedro Carneiro Junior - pedrokarneiro.bsa@gmail.com
# NOTES: Will not run with F5 from within IDLE,
# ------ Will run only by "python HelloWorld.py" command in command line.
#########################################################################

from kivy.app import App           # This is the app itself.
from kivy.uix.button import Button # This is the button to be shown.

class Test(App):                   # This class inherits from App.
    def build(self):               # This is the constructor that shows the button in the app.
        return Button(text='Hello world!')

Test().run()                       # This calls the run method of the Test class.
