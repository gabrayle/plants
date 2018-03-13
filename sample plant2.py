#sample by itself
import random
def list(plant_list):
    if len(plant_list) == 0:
        print("There are not plants to display.\n")
        return
    else:
        i = 1
        for row in plant_list:
            print(str(i) + ". " + row[0] + " ("
                  + str(row[1]) + ")")
            i +=1
        print()
def add(plant_list):
    name = input("Plant Name:  ")
    biome = input("Biome:  ")
    plant = []
    plant.append(name)
    plant.append(biome)
    plant_list.append(plant)
    print(plant[0] + " was added.\n")
def delete(plant_list):
    number = int(input("Number: "))
    if number <1 or number > len(plant_list):
        print("Invalid plant number. Please try again.\n")
    else:
        plant = plant_list.pop(number-1)
        print(plant[0] + " was deleted.\n")
        
def display_menu():
    print("COMMAND MENU")
    print("list - List all plants.")
    print("add - Add a plant.")
    print("del - Delete a plant.")
    print("exit - Exit the program.")
    print()
def main():
    plant_list = []
    display_menu()
    while True:
        command = input("What would you like to do?  ")
        if command == "list":
            list(plant_list)
        elif command == "add":
            add(plant_list)
        elif command == "del":
            delete(plant_list)
        elif command == "exit":
            break
        else:
            print("Unrecognized. Please try again.\n")
    print("Goodbye")
if __name__ == "__main__":
    main()
                   
