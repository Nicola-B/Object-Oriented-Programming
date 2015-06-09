#Nicola Batty
#09/06/2015
#Virtual Pet

class VirtualPet:
    def __init__(self, name):
        self.name = None
        self.size = 5
        self.age = 0
        self.energy = 50
        self.foods = ["biscets", "orenges", "postasheose"]
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
                print("mmmmmmmmmmm postasheose")
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

Name = input("What would you like to call your pet?: ")
YourVirtualPet = VirtualPet(Name)
Stats = []
hunger = YourVirtualPet.HungerStats()
age = YourVirtualPet.AgeStats()
mood = YourVirtualPet.MoodStats()
tired = YourVirtualPet.TiredStats()
heth = YourVirtualPet.HethStats()
