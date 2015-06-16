#Nicola Batty
#16/06/2015
#Widget

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameWidget(QWidget):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.Username = QLineEdit()
        self.Lable = QLabel("Please ener your name: ")
        self.Submit = QPushButton("Submit")
        self.Layout = QVBoxLayout()
        self.Layout.addWidget(self.Lable)
        self.Layout.addWidget(self.Username)
        self.Layout.addWidget(self.Submit)
        self.setLayout(self.Layout)
        self.Submit.clicked.connect(self.Submit_Pushed)

    def Submit_Pushed(self):
        self.NameEntered.emit()
