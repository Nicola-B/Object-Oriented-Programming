#Nicola Batty
#29/07/2015
#Farm simulation graphic animal item class

from Farm_simulation_graphic_field_item_class import *

class AnimalGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    #This class procides a pixmap item with a preset image for the animal

    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.animal = None

    def update_status(self):
        if self.animal.status == "Baby":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWith(25,1))
        elif self.animal.status == "Poor":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWith(25,1))
        elif self.animal.status == "Fine":
            self.setPixmap(QPixmap(self.available_graphics[2]).scaledToWith(25,1))
        elif self.animal.status == "Prime":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWith(25,1))

    def needs(self):
        return self.animal.needs()

    def grow(self, feed, water):
        self.animal.grow(feed, water)

    def _remove_animal(self):
        self.scene().remove_animal(self)
        
    def contextMenuEvent(self, event):
        menu = QMenu("Animal")
        remove = menu.addAction("Remove Animal")

        #connection
        remove.triggered.connect(self._remove_animal)

        #runmenu
        menu.exec_(event.screenPos())
