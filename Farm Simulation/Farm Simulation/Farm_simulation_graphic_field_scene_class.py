#Nicola Batty
#30/07/2015
#Farm simulation graphic field scene class

from PyQt4.QtGui import *

from Farm_simulation_Fields import *
from Farm_simulation_graphic_wheat_item_class import*
from Farm_simulation_graphic_potato_item_class import*
from Farm_simulation_graphic_cow_item_class import*
from Farm_simulation_graphic_sheep_item_class import*

import resources

class FieldGraphicsScene(QGraphicsScene):
    #This class procides a scene to manage items in the field

    #constructor
    def __init__(self, max_crops, max_animals):
        super().__init__()

        self.field = Field(max_crops, max_animals)

        self.background_brush = QBrush()
        self.background_picture = QPixmap(":/field_background.png")
        self.background_brush.setTexture(self.background_picture)
        self.setBackgroundBrush(self.background_brush)
