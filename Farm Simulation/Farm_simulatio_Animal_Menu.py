#Nicola Batty
#02/07/2015
#Farm simulation animation manu 

from Farm_simulation_Animal_Cows import *
from Farm_simulation_Animal_Sheep import *
from Farm_simulation_Animal_Main_Program import *

def display_menu():
    print()
    print("Which crop whould you like to create?")
    print()
    print("1) Cow")
    print("2) Sheep")
    print()
    print("Please select an option from the above menu") 

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option seleced: "))
            if choice in (1,2):
                print()
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_animal():
    display_menu()
    choice = select_option()
    Name = input("What would you like to call your new animal: ")
    print()
    if choice == 1:
        new_animal = Cow(Name)
    elif choice == 2:
        new_animal = Sheep(Name)
    return new_animal

def main():
    new_animal = create_animal()
    manage_animal(new_animal)

if __name__ == "__main__":
    main()
