#Nicola Batty
#16/06/2015
#Window

from Widget_2 import *
from NameWidget import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        #use super class
        super().__init__()

        #set name and hello wiggets
        self.name_widget = NameWidget()
        self.hello_widget = NameWidget_2()

        #Create stacked layout
        self.stack = QStackedLayout()
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.hello_widget)

        #set stacked layout as central widget
        self.widget = QWidget()
        self.widget.setLayout(self.stack)
        self.setCentralWidget(self.widget)

        #connect to the puss bottons inside the two widgets
        self.name_widget.NameEntered.connect(self.name_provided)
        self.hello_widget.Back.connect(self.back_button_cliked)
        
    def name_provided(self):
        #changing from one widget to anuther
        self.stack.setCurrentIndex(1)
        name = self.name_widget.Username.text()
        self.hello_widget.Lable.setText("Hello {0}".format(name))

    def back_button_cliked(self):
        self.stack.setCurrentIndex(0)
        #clearing the username box for next use
        self.name_widget.Username.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MyWindow()
    Window.show()
    Window.raise_()
    app.exec_()
