#Nicola Batty
#12/06/2015
#Farm Simulation Crops Main Program 

from Farm_simulation_Crop import *
from Farm_simulation_Crop_Wheat import *
from Farm_simulation_Crop_Potato import *

def auto_grow(crop, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1<= light <= 10:
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
    crop.grow(light, water)

def display_menu():
    print("1) Grow manually over 1 day")
    print("2) Grow auomatically over 30 days")
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
            print("Please enter a walid options")
    return choice

def make_menu_choice(crop, option, noexit):
    if option == 1:
        manual_grow(crop)
        print()
    elif option == 2:
        auto_grow(crop, 30)
        print()
    elif option == 3:
        print(crop.report())
        print()
    elif option == 0:
        noexit = False
        print()
    return noexit

def manage_crop(crop):
    print("This is the crop management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option =  get_menu_choice()
        print()
        noexit = make_menu_choice(crop, option, noexit)
    print("Thank you for using the crop management program")

def main():
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
