#Nicola Batty
#01/07/2015
#Farm simulation Animal Main Program

import random

from Farm_simulation_Animal import *
from Farm_simulation_Animal_Cows import *
from Farm_simulation_Animal_Sheep import *

def auto_days(animal, days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_day(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1<= food <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1<= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    animal.grow(food, water)

def display_menu():
    print("1) Manage animal manuly for 1 day")
    print("2) Manage animal for 30 days")
    print("3) Report status")
    print("0) Exit test program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0<= choice <= 3:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid options")
    return choice

def make_menu_choice(animal, option, noexit):
    if option == 1:
        manual_day(animal)
        print()
    elif option == 2:
        auto_days(animal, 30)
        print()
    elif option == 3:
        print(animal.report())
        print()
    elif option == 0:
        noexit = False
        print()
    return noexit

def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option =  get_menu_choice()
        print()
        noexit = make_menu_choice(animal, option, noexit)
    print("Thank you for using the animal management program")

def main():
    new_animal = Animal(1,4,3, Name)
    manage_animal(new_animal)

#so if I set this program to run it will run starting from this one
if __name__ == "__main__":
    main()
