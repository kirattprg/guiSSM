'''
First PyQt5 (PySide5) app

Created by Phil J Sept 25

Note - no apparent distro for PySide 6 via pip - so cant install to use with Thonny, yet.

This will also run with Win11, assuming the PyQt5 lib files are installed with Thonny

resource - raspberrytips.com/pyqt-on-raspberry-pi

*****
      To begin run this script as is - after running the code, add comments to these
      uncommented lines (not the from or import), describing what happens
      
      Upload the completed code with comments to your github, provide the url in the DC Connect assignment box
*****
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton  # Importing necessary GUI components
import sys  # Import system module for application exit handling

app = QApplication([])  # Create the application object; required for any PyQt5 GUI app
win = QMainWindow()  # Create a main window object

# 2nd section 
win.setWindowTitle("A windows thing")  # Set the text that appears in the window's title bar
win.resize(500, 500)  # Set the window size to 500px by 500px
win.move(400, 200)  # Position the window on the screen at coordinates (400, 200)

# 3rd section 
label = QLabel("Some text", win)  # Create a text label with "Some text" and place it inside the window
label.move(50, 100)  # Position the label at coordinates (50, 100) within the window

# 4th section 
def clickMethod():  # Define a function that will run when the button is clicked
   print("Button clicked")  # This prints a message to the console when the button is clicked

button = QPushButton("Click here", win)  # Create a button with the label "Click here" and add it to the window
button.move(20, 40)  # Position the button at coordinates (20, 40) in the window
button.clicked.connect(clickMethod)  # Connect the button's click event to the clickMethod function

win.show()  # Display the window on the screen

sys.exit(app.exec_())  # Start the event loop, and cleanly exit the app when the window is closed
