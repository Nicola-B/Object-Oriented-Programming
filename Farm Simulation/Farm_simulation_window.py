#Nicola Batty
#17/06/2015
#Farm simulation window

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Farm_simulation_radio_button_widget import *

class CropWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ctop Simulator")

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()
