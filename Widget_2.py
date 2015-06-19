#Nicola Batty
#16/06/2015
#Widget_2

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameWidget_2(QWidget):
    Back = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.Lable = QLabel(None)
        self.Button = QPushButton("Back")
        self.Layout = QVBoxLayout()
        self.Layout.addWidget(self.Lable)
        self.Layout.addWidget(self.Button)
        self.setLayout(self.Layout)
        self.Button.clicked.connect(self.Back_Pushed)

    def Back_Pushed(self):
        self.Back.emit()
