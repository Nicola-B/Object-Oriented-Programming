#Nicola Batty
#12/06/2015
#Farm simulation Crop Wheat 

from Farm_simulation_Crop import *

class Wheat(Crop):
    """A wheat food crop"""
    def __init__(self):
        super().__init__(1,3,6)
        self._type = "wheat"
