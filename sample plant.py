#sample by itself
import random
print ("Welcome to your random plant finder.") 
print()
    #ask user to input biome type
def display_menu():
    print("COMMAND MENU")
    print("list - List all Biomes")
    print("add - Add a Biome")
    print("del - Delete a Biome")
    print("exit - Exit program")
    print()
    
def list(biome_list):
    i = 1
    for biome in biome_list:
        print(str(i) + ". " + biome)
        i +=1
    print()

def add(biome_list):
    biome = input("Biome Name:      ")
    biome_list.append(biome)
    print(biome + " was added. \n")
    
def delete(biome_list):
    number = int(input("Number:  "))
    if number <1 or number >len(biome_list):
        print("Invalid biome number.\n")
    else:
        biome = biome_list.pop(number-1)
        print(biome + " was deleted. \n")
def main():
    biome_list = ["Tundra",
                  "Grassland"]

    display_menu()
    while True:
        command = input("Command:  ")
        if command.lower() == " list":
            list(biome_list)
        elif command.lower() == "add":
            add(biome_list)
        elif command.lower() == "del":
            delete(biome_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.")
    print("Farewell.")       
if __name__ == "__main__":
    main()
