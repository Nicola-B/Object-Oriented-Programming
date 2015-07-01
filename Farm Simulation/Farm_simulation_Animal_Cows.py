#Nicola Batty
#01/07/2015
#Farm simulation Animal Cows

from Farm_simulation_Animal import *

class Cow(Animal):
    # a cow
    def __init__(self, Name):
        super().__init__(Name, 5, 6, 7)
        self.type = "Cow"

    def grow(self, food, water):
        if food >= self.food_need and water >= self._waterneed:
            if self.status == "thiner then normal" and food > self.food_need:
                self.growth += self.growth_rate * 1.25
            elif self.status == "thin and food > self.food_need:
                self.growth += self.growth_rate * 1.5
            else:
                self.growth += self.growth_rate
        self.days_growing += 1
        self.update_status()
