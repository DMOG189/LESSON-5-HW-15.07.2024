# LESSON 5 EX 6 TARGIL 4 IMPORT/RANDOM

# random an int number between 1-100 (nim1)
# random a second int number between 1-100 (num2) 100
# print an exrecise num1 + num2 = ?
#                   40   + 100  = 140
# ask input from user
# check if the user answered correctly
# run it in a loop until the user answer correct

# START

import random

num2 = 100

while True:
    num1 = random.randint(1, 100)

    print(f"{num1} + {num2} = ?")

    user_answer = int(input("Your answer: "))

    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print("Correct!")
        break
    else:
        print(f"Incorrect. The correct answer is {correct_answer}. Try again.")

# END


# 23 + 100 = ?
# Your answer: 100
# Incorrect. The correct answer is 123. Try again.
# 54 + 100 = ?
# Your answer: 154
# Correct!

