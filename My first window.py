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
        super().__init__()
        self.name_widget = NameWidget()
        self.hello_widget = NameWidget_2()
        self.setCentralWidget(self.name_widget)
        self.name_widget.NameEntered.connect(self.name_provided)

    def name_provided(self):
        self.setCentralWidget(self.hello_widget)
        name = self.name_widget.Username.text()
        self.hello_widget.Lable.setText(name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MyWindow()
    Window.show()
    Window.raise_()
    app.exec_()
