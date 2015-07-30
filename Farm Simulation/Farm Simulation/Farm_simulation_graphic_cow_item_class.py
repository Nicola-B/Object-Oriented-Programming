#Nicola Batty
#30/07/2015
#Farm simulation graphic cow item class

from Farm_simulation_graphic_animal_item_class import*
from Farm_simulation_Animal_Cows import *

import resources

class CowGraphicsPixmapItem(AnimalGraphicsPixmapItem):
    #This class procides a graphical representation of a cow

    #constructor
    def __init__(self):
        self.available_graphics = [":/cow_baby.png", ":/cow_poor.png",
                                   ":/cow_fine.png", ":/cow_prime.png"]

        super().__init__(self.available_graphics)

        self.animal = Cow("")
