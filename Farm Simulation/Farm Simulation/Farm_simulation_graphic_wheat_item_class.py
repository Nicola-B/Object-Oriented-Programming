#Nicola Batty
#30/07/2015
#Farm simulation graphic wheat item class

from Farm_simulation_graphic_crop_item_class import *
from Farm_simulation_Crop_Wheat import *

import resources

class WheatGraphicsPixmapItem(CropGraphicsPixmapItem):
    #This class provides a graphicalrepresentation of a wheat crop

    #constructor
    def __init__(self):
        self.available_graphics = [":/wheat_seed.png", ":/wheat_seedling.png",
                                   ":/wheat_young.png", ":/wheat_mature.png",
                                   ":/wheat_old.png"]
        super().__init__(self.available_graphics)

        self.crop = Wheat()
