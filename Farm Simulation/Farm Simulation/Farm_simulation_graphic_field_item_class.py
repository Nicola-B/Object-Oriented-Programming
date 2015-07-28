#Nicola Batty
#28/07/2015
#Farm simulation graphic field item class

from PyQt4.QtGui import *

class FieldItemGraphicsPixmapItem(QGraphicsPixmapItem):
    #This class procides a pixmap item with a preset image for the item

    #constructor
    def __init__(self, graphics_list):
        super().__init__()
        self.available_graphics = graphics_list
        self.current_graphic = QPixmap(self.available_graphics[0])
        self.setPixmap(self.current_graphic.scaledToWidth(25,1))
        self.setFlag(QGraphicsItem.ItemIsMocable) #allows us to move the graphic in ths scene

    def update_status(self):
        pass
