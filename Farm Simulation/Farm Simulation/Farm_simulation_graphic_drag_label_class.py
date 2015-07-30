#Nicola Batty
#30/07/2015
#Farm simulation graphic drag label class

from PyQt4.QtGui import *

import resources

class QDragLabel(QLabel):
    #This class provides an image label that can be dragged and dropped

    #constructor
    def __init__(self, picture):
        super().__init__()
        self.setPixmap(picture.scaledToWidth(35,1))

class WheatDragLabel(QDragLabel):
    #This class provides a wheat label taht can be dragged and dropped

    def __init__(self):
        super().__init__(QPixmap(":/wheat_seed.png"))

class PotatoDragLabel(QDragLabel):
    #This class provides a potato label taht can be dragged and dropped

    def __init__(self):
        super().__init__(QPixmap(":/potato_seed.png"))

class CowDragLabel(QDragLabel):
    #This class provides a Cow label taht can be dragged and dropped

    def __init__(self):
        super().__init__(QPixmap(":/cow_baby.png"))

class SheepDragLabel(QDragLabel):
    #This class provides a sheep label taht can be dragged and dropped

    def __init__(self):
        super().__init__(QPixmap(":/sheep_baby.png"))
