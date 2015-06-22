#Nicola Batty
#15/06/2015
#Virtual Pet Dog 

from Virtual_Pet_Bace import *

class Dog(VirtuaPet):
    def __init__(self, name):
        super.__init__(name)
        self.size = 8
        self.food = ["Dog biscets", "Wet food", "Orenges"]
        
