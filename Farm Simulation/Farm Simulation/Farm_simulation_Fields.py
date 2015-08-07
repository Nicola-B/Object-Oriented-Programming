#Nicola Batty
#07/07/2015
#Farm simulation Fields

from Farm_simulation_Crop_Potato import *
from Farm_simulation_Crop_Wheat import *
from Farm_simulation_Animal_Cows import *
from Farm_simulation_Animal_Sheep import *

class Field:
    #Simulate a field that can contain animals and crops

    #constructor
    def __init__(self, max_animals, max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self, position):
        return self._crops.pop(position)
    
    def remove_animal(self, position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"crops": crop_report, "animals":animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        for animal in self._animals:
            need = animal.needs()
            food += needs["food need"]
            if needs["water need"] > water:
                water = needs["water need"]
            return{"food": food, "light": light, "water": water}
    
    def grow(self, light, food, water):
        #grow the cros (light and water are available to all crops in same amont
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light, water)
        if len(self._animals) > 0:
            #grow the animals(water available to all animals in same amounts
            #but food is a total that must be shared
            food_required = 0
            #get a toal of the food required by the animals in the field
            for animal in self._animals:
                needs = animal.needs()
                food += needs["food need"]
            #if we have more food available than is requred work out the addition
            #available food

def main():
    new_field = Field(5,2)
    new_field.plant_crop(Wheat())
    new_field.plant_crop(Potato())
    new_field.add_animal(Sheep("Shaun"))
    new_field.add_animal(Cow("Jim"))
    print(new_field._crops)
    print(new_field._animals)

if __name__== "__main__":
    main()
