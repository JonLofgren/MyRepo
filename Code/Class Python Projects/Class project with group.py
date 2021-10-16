person = []
prices = []
flag = False


def user_input():
    global flag
    person1 = input("What is the person's name?\n")
    while True:
        try:
            price1 = float(input(f"How much did {person1} spend on food?\n"))
            person.append(person1)
            prices.append(price1)
            break
        except ValueError:
            print("Please input a number!")
    flag = True


def print_lists():
    price_sum = 0
    if not flag:
        print("There are no people entered!\n")
    else:
        for num in range(len(person)):
            print(f"{person[num]}'s cost for food is ${prices[num]}.")
            price_sum += prices[num]
        price_average = round(price_sum/len(prices), 2)
        print(f"\nThe average cost for food is ${price_average}.\n")
        for num in range(len(person)):
            if prices[num] > price_average:
                print(f"{person[num]} spent ${round(prices[num], 2)} on food. That is more than the average cost on food!")
            elif prices[num] < price_average:
                print(f"{person[num]} spent ${round(prices[num], 2)} on food. That is less than the average cost on food!")
            elif prices[num] == price_average:
                print(f"{person[num]} spent ${round(prices[num], 2)} on food. That is the average cost on food!")
        print()


def main():
    while True:
        choice = input("Add a person - a\nList prices - b\nExit (does not save data) - c\n").lower()
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
