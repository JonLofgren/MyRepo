"""class Pet:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color


dog = Pet("Malachi", "great pyrneese", "black and white")
cat = Pet("Esper", "bangle", "orange with brown spots")
print(f"{dog.name} is a {dog.breed} and is {dog.color}")
print(f"{cat.name} is a {cat.breed} and is {cat.color}")"""

class Pet:
    def __init__(self):
        self.classname = input("What is the class name?\n")
        self.name = input("What is your pet's name?\n")
        self.breed = input(f"What is {self.name}'s breed?\n")
        self.color = input(f"What is {self.name}'s color?\n")

cat = Pet()
print(f"{cat.name} is a {cat.breed} and is {cat.color}")

index = 0
test = []
while True:
    choice = input("More? Y|n\n").lower()
    if choice == "y" or choice == "":
        name = input("What is the class name?\n")
        test.append(name)
        test[index] = Pet()
        index += 1
    elif choice == "n":
        for word in test:
            print(f"Class name is {word.classname} and the pet's name is {word.name}, breed of {word.breed}, and a color of {word.color}")
        break
    else:
        print("Invalid input!")
