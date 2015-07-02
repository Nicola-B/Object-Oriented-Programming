#Nicola Batty
#01/07/2015
#Farm simulation Animal

class Animal:
    #A farm animal
    def __init__(self, Name, food_need, water_need, growth_rate):
        self.weight = 0
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self.status = "thin"
        self.type = "farm animal"
        self.name = Name

    def needs(self):
        return {"food meed":self.food_need, "water need":self.water_need}

    def report(self):
        return {"name":self.name, "type":self.type, "status":self.status, "days growing":self.days_growing, "weight":self.weight}

    def update_status(self):
        if self.weight > 32:
            self.status = "obese"
        elif self.weight > 22:
            self.status = "fat"
        elif self.weight > 12:
            self.status = "normal"
        elif self.weight > 2:
            self.status = "thiner then normal"
        elif self.weight == 2:
            self.status = "thin"

    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            self.weight += self.growth_rate
        self.days_growing += 1
        self.update_status()
