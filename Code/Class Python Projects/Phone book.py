def user_input():
    name = input("What is the person's name?\n")
    email = input(f"What is {name}'s email?\n")
    number = input(f"What is {name}'s phone number?\n")
    with open("contacts.txt", "a") as file:
        file.write(f"{name}'s email is {email}, and a phone number of {number}.\n")


def print_lists():
    with open("contacts.txt", "r") as file:
        print(file.read())


def main():
    while True:
        choice = input("Add a person to the book - a\nPrint book people - b\nExit - c\n").lower()
        if choice == "a":
            user_input()
        elif choice == "b":
            print_lists()
        elif choice == "c":
            break
        else:
            print("Invalid input!\n")


if __name__ == "__main__":
    main()
else:
    exit()
