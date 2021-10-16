with open("saved.txt", "a") as file:
    count = 0
    while True:
        file.write(f"This is the {count} line\n")
        count += 1

  #  with open("saved.txt", "r") as file:
   #     print(file.read())