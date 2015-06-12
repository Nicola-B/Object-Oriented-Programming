#Nicola Batty
#12/06/2015
#Farm simulation Crop Potato

from Farm simulation Crop import *

class Potato(Crop):
    """A potato food crop"""
    def __init__(self):
        super.__init__(1,3,6)
        self._type = "potato"

    def grow(self, light, water):
        if light >= slef._light_need and water >= slef._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif slef._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
