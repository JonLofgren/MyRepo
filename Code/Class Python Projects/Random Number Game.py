import random

atempts = 0
def num_choice():
    while True:
        try:
            choice = int(input("Pick a whole number between 1 and 100\n"))
            if choice < 1 or choice > 100:
                print("Number needs to be between 1 and 100\n")
                continue
            else:
                 return choice
        except ValueError:
            print("Pick a valid number yo\n")

def play_game():
    rand_num = random.randint(1, 100)
    #print(f"The random number is {rand_num}.")
    atempts = 0
    while atempts < 5:
        num = num_choice()
        if num == rand_num:
            print("You win! You guessed the pseudorandom number!\n")
            break
        elif num > rand_num:
            print("Your choice was too high!")
        elif num < rand_num:
            print("Your choice was too low!")
        atempts += 1

    if atempts == 5:
        print(f"You loose! The correct number was {rand_num}!\n\n")


print("Welcome to Guessing Game™!")
play_game()
while True:
    is_playing = input("Do you want to play again? Y|n\n").lower()
    if is_playing == "y" or is_playing == "":
        play_game()
    elif is_playing == "n":
        print("Exiting")
        break
    else:
        print("Please input a valid choice!\n")