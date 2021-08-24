def is_num(question):
    while True: # checks if the input is an int, if not, ask for another input
        try:
            x = int(input(question))
            break
        except ValueError:
            print("That is not a number")
            continue
    return x

class cat():
    def __init__(self): # asks the questions about the pet
        self.name = input("\nWhat is your pet's name?\n")
        self.type = input(f"What type of pet is {self.name}?\n").lower()
        self.color = input(f"What color is {self.name}?\n").lower()
        self.age = is_num(f"How old is {self.name}?\n")

def main():
    pet = [] # initialize the list called pet
    response = "y"
    name = input("Hello! What is your name?\n") # sets name equal to what user inputs
    while response != "n": # checks if you have another pet and loops if you do
        pet.append(cat()) # calls the function cat() to ask the pet questions and appends to pet
        while True: # checks if user gives a valid input
            response = input("\nDo you have another pet? Y|n: ").lower()
            if response == "y" or response == "":
                break
            elif response == "n":
                break
            else:   # basically, this while loop sets response to 'y' or 'n' and keeps asking if user does not give correct input
                print("\nYou did not make a correct response, please use a 'Y' for yes and a 'n' for no.")
                continue
    num_pets = len(pet) #checks the length of the list of pets to see how many total the user put in
    with open('My_Pet_List.txt','w') as file: # opens the file in write mode, and if the file does not exist, creates one
        if num_pets == 1:
            file.write(f"{name} has one pet, it's name is {pet[0].name}.\n\n") # if the number of pets is one, it will make pets singular
        else:
            file.write(f"{name} has {num_pets} pets. Those pet's names are:") # if more than one, plural
            count = 0 # sets variable equal to zero
            for i in pet:
                count += 1 # increments count to the size of pet
                if count == 1:
                    file.write(f" {i.name}") # if it is just one pet, names do not need to be comma separated
                elif count != 1:
                    file.write(f", {i.name}") # comma separated if more than one pet
            file.write(".\n\n") # writes new lines on the txt file
        for i in pet:
            file.write(f"{i.name} is a {i.color} {i.type} and is {i.age} years old.\n")
            # ^^^ compiles the inputted data into a more human readable format

#where the code starts
if __name__ != "__main__":
    main() #calls the main loop
else:
    exit()
