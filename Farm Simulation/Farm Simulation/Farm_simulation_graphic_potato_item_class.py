#Nicola Batty
#30/07/2015
#Farm simulation graphic potato item class

from Farm_simulation_graphic_crop_item_class import *
from Farm_simulation_Crop_Potato import *

import resources

class PotatoGraphicsPixmapItem(CropGraphicsPixmapItem):
    #This class provides a graphicalrepresentation of a potato crop

    #constructor
    def __init__(self):
        self.available_graphics = [":/potato_seed.png", ":/potato_seedling.png",
                                   ":/potato_young.png", ":/potato_mature.png",
                                   ":/potato_old.png"]
        super().__init__(self.available_graphics)

        self.crop = potato()

