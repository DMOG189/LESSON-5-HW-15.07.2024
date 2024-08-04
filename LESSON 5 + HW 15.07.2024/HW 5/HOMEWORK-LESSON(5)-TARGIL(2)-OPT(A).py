# HOMEWORK LESSON 5 TARGIL 2 OPTION A

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

def play_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        if guess > target_number:
            print("The number is too big")
        elif guess < target_number:
            print("The number is too small")
        else:
            print("BINGO")
            print(f"You guessed the number in {attempts} attempts.")
            break


while True:
    play_game()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")


# END