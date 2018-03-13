FILENAME = "plants.txt"

def write_plants(plants):
    with open(FILENAME, "w") as file:
        for plant in plants:
            file.write(plant + "\n")
def read_plants():
    plants = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            plants.append(line)
    return plants
def list_plants(plants):
    for i in range(len(plants)):
        plant = plants[i]
        print(str(i+1) + ". " + plant)
    print()
def add_plant(plants):
    name = input("Plant Name:  ")
    plant = []
    plants.append(name)
    write_plants(plants)                   
    print(plants[0] + " was added.\n")
def delete_plant(plants):
    index = int(input("Number: "))
    plant = plants.pop(index - 1)
    write_plants(plants)
    print(plant + " was deleted.\n")
def display_menu():
    print("COMMAND MENU")
    print("list - List all plants.")
    print("add - Add a plant.")
    print("del - Delete a plant.")
    print("exit - Exit the program.")
    print()
def main():
    display_menu()
    plants = read_plants()
    while True:
        command = input("Command: ")
        if command == "list":
            list_plants(plants)
        elif command == "add":
            add_plant(plants)
        elif command == "del":
            delete_plant(plants)
        elif command == "exit":
            print("Farewell.")
            break
        else:
            print("Not a valid command. Please try again.") 
if __name__ == "__main__":
     main()
