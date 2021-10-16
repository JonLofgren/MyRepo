stores = []
questions = ["How many 100's do you have?\n", "How many 50's do you have?\n", "How many 20's do you have?\n",
             "How many 10's do you have?\n", "How many 5's do you have?\n", "How many 1's do you have?\n",
             "How many quarters do you have?\n", "How many dimes do you have?\n", "How many nickles do you have?\n",
             "How many pennies do you have?\n"]
value = [100, 50, 20, 10, 5, 1, .25, .1, .05, .01]


# Creates the data for each location added
class Locations:
    def __init__(self):
        self.location_name = input("What is the name of this location?\n")
        self.total = 0

    def add(self):
        self.total = 0
        count = 0
        # Goes through and adds the money to the total
        while True:
            try:
                self.total += int(input(questions[count])) * value[count]
                count += 1
                if count == len(questions):
                    break
            except ValueError:
                print("Please input a valid number!")
        print(f"The total at {self.location_name} is ${round(self.total, 2)}.\n")


# Allows for the user to pick a location for use later
def list_locations():
    # Prints a list from 0 to however many item are in stores[] for the user to pick
    while True:
        try:
            print("Which store would you like?")
            for i in range(len(stores)):
                print(f"{i}) {stores[i].location_name}")
            choice = int(input("----> "))
            if choice not in range(len(stores)):
                print("Please input a valid choice!")
                continue
            else:
                return choice  # Returns the value to be used as an index in stores[]
        except ValueError:
            print("Please input a valid choice!")


# Prints the data for all locations and asks if the user wants to save it to a file
def print_data():
    grand_total = 0
    for i in range(len(stores)):  # Shows the totals for all locations and the grand total of all of them
        grand_total += stores[i].total
        print(f"The last logged total for {stores[i].location_name} is ${round(stores[i].total, 2)}.")
    print(f"The grand total for all locations is ${round(grand_total, 2)}\nThe average for all locations is "
          f"${round(grand_total/len(stores), 2)}.")
    # Saves the same data to a file if the user wants to
    while True:
        choice = input("Would you like to save this information to a text file? Y|n\n").lower()
        if choice == "y" or choice == "":
            with open("store_totals.txt", "w") as f:
                for i in range(len(stores)):
                    f.write(f"The last logged total for {stores[i].location_name} is ${round(stores[i].total, 2)}.\n")
                f.write(f"The grand total for all locations is ${round(grand_total, 2)}.\nThe average for all "
                        f"locations is ${round(grand_total/len(stores), 2)}.")
            break
        elif choice == "n":
            break
        else:
            print("Please input a valid choice!")


# User selection for what to do
def main():
    while True:
        selection = input("a) Add a store location\nb) Update values\nc) Print/save data\nd) Exit\n").lower()
        if selection == "a":
            stores.append(Locations())  # Creates the name for the location
            stores[-1].add()  # Adds the data to that location
        elif selection == "b":
            if len(stores) == 0:
                print("There are no stores to update!")
            else:
                stores[list_locations()].add()  # Updates the values in the location picked by the user
        elif selection == "c":
            if len(stores) == 0:
                print("There are no stores entered!")
            else:
                print_data()
        elif selection == "d":
            rethinking_life = input("Exiting does not save data. Would you like to go back? Y|n\n").lower()
            if rethinking_life == "y" or rethinking_life == "":
                continue
            elif rethinking_life == "n":
                exit()
            else:
                print("Invalid input")
        else:
            print("Please input a valid choice!")


if __name__ == "__main__":
    main()
else:
    exit()
