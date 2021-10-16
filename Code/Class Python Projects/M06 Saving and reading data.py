open("mood.txt", "a").close()

with open("mood.txt", "r") as file:
    contents = file.read()
    if len(contents) > 0:
        print(f"Last time you had a {contents} day.\n")

with open("mood.txt", "w") as file:
    while True:
        choice = input("How is your day today? Good or bad.\n").lower()
        if choice == "good" or choice == "bad":
            break
        else:
            print("Invalid input!\n")
    file.write(choice)
