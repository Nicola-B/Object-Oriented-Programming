#Nicola Batty
#29/07/2015
#Farm simulation graphic animal item class

from Farm_simulation_graphic_field_item_class import *

class AnimalItemGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    #This class procides a pixmap item with a preset image for the animal

    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.animal = None

    def update_status(self):
        if self.animal._status == "Baby":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWith(25,1))
        elif self.animal._status == "Poor":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWith(25,1))
        elif self.animal._status == "Fine":
            self.setPixmap(QPixmap(self.available_graphics[2]).scaledToWith(25,1))
        elif self.animal._status == "Prime":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWith(25,1)

    
