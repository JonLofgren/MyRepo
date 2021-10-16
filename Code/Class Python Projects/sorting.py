from random import randint, shuffle
from time import sleep, time
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def display(arr):
    clear()
    for i in range(len(arr)):
        for _ in range(arr[i]): print("-", end="")
        print()


def sort(arr):
    display(arr)
    for i in range(len(arr)):
        start = i + 1
        for j in range(start, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                display(arr)


def main():
    clear()
    arr = []
    while True:
        try:
            len = int(input("How many items do you want to sort?\n"))
            break
        except ValueError:
            print("Please input a valid number!")
    for i in range(len):
        arr.append(i + 1)
    shuffle(arr)
    clear()
    start = time()
    sort(arr)
    print(f"\nTime to complete: {time() - start} seconds")


if __name__ == "__main__":
    main()
