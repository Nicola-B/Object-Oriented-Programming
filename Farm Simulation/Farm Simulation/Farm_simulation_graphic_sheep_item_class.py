#Nicola Batty
#30/07/2015
#Farm simulation graphic sheep item class

from Farm_simulation_graphic_animal_item_class import*
from Farm_simulation_Animal_Sheep import *

import resources

class SheepGraphicsPixmapItem(AnimalGraphicsPixmapItem):
    #This class procides a graphical representation of a sheep

    #constructor
    def __init__(self):
        self.available_graphics = [":/sheep_baby.png", ":/sheep_poor.png",
                                   ":/sheep_fine.png", ":/sheep_prime.png"]

        super().__init__(self.available_graphics)

        self.animal = Sheep("")

