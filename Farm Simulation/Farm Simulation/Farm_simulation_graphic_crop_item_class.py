#Nicola Batty
#28/07/2015
#Farm simulation graphic crop item class

from Farm_simulation_graphic_field_item_class import *

class CropItemGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    #This class procides a pixmap item with a preset image for the crop

    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.crop = None

    def update_status(self):
        if self.crop._status == "Seed":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWith(25,1))
        elif self.crop._status == "Seedling":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWith(25,1))
        elif self.crop._status == "Young":
            self.setPixmap(QPixmap(self.available_graphics[2]).scaledToWith(25,1))
        elif self.crop._status == "Mature":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWith(25,1))
        elif self.crop._status == "Old":
            self.setPixmap(QPixmap(self.available_graphics[4]).scaledToWith(25,1))

    
