#Nicola Batty
#09/06/2015
#Virtual Pet Bace 

class VirtualPet:
    def __init__(self, name):
        self.name = None
        self.size = 5
        self.age = 0
        self.energy = 50
        self.foods = [None]
        self.mood = 5
        self.tired = 5
        self.heth = 10

    def eat(self, food, stats):
        if stats 
        if food is self.foods:
            if food == self.foods[0]:
                self.energy = self.energy + 20
                self.mood = self.mood + 1
                print("num num")
            elif food == self.foods[1]:
                self.energy = self.energy + 30
                self.mood = self.mood + 2
                print("yum")
            elif food == self.foods[2]:
                self.energy = self.energy + 10
                self.mood = self.mood + 3
                print("mmmmmmmmmmm {0}".format(self.foods[2])
        else:
            print("I'm not eating that")
            self.mood = self.mood - 1

    def HungerStats(self):
        if self.energy > 100:
            hunger = "full, not up for a work"
        elif self.energy > 50:
            hunger = "Need a work"
        elif self.energy == 50:
            hunger = "Ok"
        elif self.energy < 50:
            hunger = "need food"
        elif self. energy < 0:
            hunger = "YOUR PET DIED OF HUNGER! YOU ARE A BAD PERSON! A VEARY BAD PERSON!"

V
