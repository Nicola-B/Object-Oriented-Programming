#Nicola Batty
#15/06/2015
#Virtual Pet Main 

from Virtual_Pet_Bace import *
from Virtual_Pet_Dog import *

Name = input("What would you like to call your pet?: ")
YourVirtualPet = VirtualPet(Name)
Stats = []
hunger = YourVirtualPet.HungerStats()
age = YourVirtualPet.AgeStats()
mood = YourVirtualPet.MoodStats()
tired = YourVirtualPet.TiredStats()
heth = YourVirtualPet.HethStats()

