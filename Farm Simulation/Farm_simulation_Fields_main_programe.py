#Nicola Batty
#13/07/2015
#Farm simulation Fields main programe

from Farm_simulation_Fields import *

def auro_grow(field, days):
    #grow the field auromatically over x days
    for day in range(days):
        light = random.randint(1,10)
        food = random.randint(1,100)
        water = random.randint(1,10)
        field.grow(light, food, water)

def manual_grow(field):
    #get the litgh, water and food values from the user
    valid = False
    while not valid:
        try:
            light = int(input("Plese enter a light value (1-10): "))
            if 1<= light <= 10:
                valid = True
            else:
                print("Value entered is not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not walid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            food = int(input("Plese enter a food value (1-100): "))
            if 1<= food <= 100:
                valid = True
            else:
                print("Value entered is not valid - please enter a value between 1 and 100")
        except ValueError:
            print("Value entered not walid - please enter a value between 1 and 100")
    valid = False
    while not valid:
        try:
            water = int(input("Plese enter a water value (1-10): "))
            if 1<= water <= 10:
                valid = True
            else:
                print("Value entered is not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not walid - please enter a value between 1 and 10")
    #grow the field
    field.grow(light, food, water)

def display_crops(crop_list):
    print()
    print("This following crops are in this field: ")
    pos = 1
    for crop in crop_list:
        print("{0:>2}) {1}".format(pos, crop.report()))
        pos += 1

def display_animal(animal_list):
    print()
    print("This following animals are in this field: ")
    pos = 1
    for animal in animal_list:
        print("{0:>2}) {1}".format(pos, animal.report()))
        pos += 1

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Plaease select a crop:"))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Plaease select an animal:"))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animals = select_animals(len(field._animals))
    return field.harvest_animals(selected_animals)

def display_crop_menu():
    print()
    print("Which crop type would you like to add?")
    print()
    print("1) Potato")
    print("2) Wheat")
    print()
    print("0) I don't want to add a crop - return me to the main menu")
    print()
    print("Please select an option from the above menu")

def display_animal_menu():
    print()
    print("Which animal type would you like too add?")
    print()
    print("1) Cow")
    print("2) Sheep")
    print()
    print("0) I don't want to add a crop - return me to the main menu")
    print()
    print("Please select an option from the above menu")

def display_main_menu():
    print()
    print("1) Plant a new crop")
    print("2) Harvest a crop")
    print()
    print("3) Add an animal")
    print("4) Remove an animal")
    print()
    print("5) Grow field manually over 1 day")
    print("6) Grow field automaticlly over 30 days")
    print()
    print("7) Report field status")
    print()
    print("8) Exit test program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice(lower, upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if lower<= choice <= upper:
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - potato not planted")
            print()
    if choice == 2:
        if field.plant_crop(Wheat()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - Wheat not planted")
            print()

def add_animal_to_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    name = input("Please give your new animal a name: ")
    if choice == 1:
        if field.add_animal(Cow(name)):
            print()
            print("Cow added")
            print()
        else:
            print()
            print("Field is full - cow not added")
            print()
    if choice == 2:
        if field.add_animal(Sheep(name)):
            print()
            print("Sheep added")
            print()
        else:
            print()
            print("Field is full - sheep not added")
            print()

def manage_field(field):
    print("This is the field management program")
    print()
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        print()
        if option == 1:
            plant_crop_in_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            print("You removed the crop: {0}". format(removed_crop))
        elif option == 3:
            add_animal_to_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            print("You removed the animal: {0}".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option == 7:
            print(field.report_contents())
            print()
        elif option == 0:
            exit = True
            print()
    print("Thank you for using the field management program")

def main():
    new_field = Field(5,2)
    manage_field(new_field)
    
    
if __name__== "__main__":
    main()
