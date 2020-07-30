# Associating Widgets
# Date created: 2020-07-2020
# \EstudoKivy\HelloWorldKivy\AssociatingWidgets.py
# Pedro Carneiro Junior - pedrokarneiro.bsa@gmail.com
# NOTES: Will not run with F5 from within IDLE,
# ------ Will run only by "python AssociatingWidgets.py" command in command line.
#################################################################################

from kivy.app import App                 # This is the app itself.
from kivy.uix.button import Button       # This is the button class.
from kivy.uix.boxlayout import BoxLayout # This is the box layout class (a container that arranges the items within it in the layout like boxes).
from kivy.uix.label import Label         # This is a label class to show text.

class Test(App):                         # This class inherits from App.
    def build(self):                     # This is the constructor that shows the button in the app.
        # We are going to show one box inside the other.
        box = BoxLayout(orientation='vertical') # This is the outter box (will be shown at the end with everything within it).
        # These objects will go in the box.
        button = Button(text = 'Button 1')
        label = Label(text='Label Text 1')
        # This method is the one that adds the button and lebal widgets to the box.
        box.add_widget(button)
        box.add_widget(label)
        # This box will go within the other box
        box2 = BoxLayout()               # Default orientation is horizontal.
        button2 = Button(text = 'Button 2')
        label2 = Label(text='Label Text 2')
        box2.add_widget(button2)
        box2.add_widget(label2)
        # This adds box2 to box.
        box.add_widget(box2)
        # This will show the outter box (and all within it) by returning it.
        return box

Test().run()                       # This calls the run method of the Test class.
