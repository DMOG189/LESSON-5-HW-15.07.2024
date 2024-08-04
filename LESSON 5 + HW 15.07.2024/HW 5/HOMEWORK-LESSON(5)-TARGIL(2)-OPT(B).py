# HOMEWORK LESSON 5 TARGIL 2 OPTOION B

# NUMBER GUESSING GAME
# random a number between 1-100
# input a guess from user until he guessed the correct number
# if a bigger number has been entered print "the number is to big"
# if a smaller number has been entered print "the number is to small"
# if the number is the exact value print "BINGO"
# NOTE!: the number isnt randomized until the user guessed the number
# at the end of the game print how manmy attempts ghas been made by user
# at the end of the game create an exit loop to the game
# until user chooses exit loop and a game loop until user guessed the correct number

# START

import random

print("Welcome to Danny's game have fun!")

while True:
    lucky_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the lucky number boy!(1, 100):"))
        attempts += 1

        if guess > lucky_number:
            print("brother eww too big")
        elif guess < lucky_number:
            print("small pp")
        else:
            print("BINGO BLYAT")
            break

    print(f"damm bro it took you {attempts} to get lucky.")

    play_again = input("Do you want to go for second round blin (cyka / blyat): ").strip().lower()
    if play_again != 'blyat' :
        print("yobane shashlik")
        break

# END