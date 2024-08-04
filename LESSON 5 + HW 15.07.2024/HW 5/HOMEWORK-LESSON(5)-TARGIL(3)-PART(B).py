# HOMEWORK LESSON 5 TARGIL 3 PART B

# NESTED LOOP PART B
# input from user a positive number bigger than 0
# print the next cimetrical shape
# improve the solution and create a loop
#           *
#          ***
#         *****
#        *******


# START

while True:
    number = int(input("Enter a positive number greater than 0 (or enter 0 to exit): "))

    if number == 0:
        print("Exiting the program.")
        break
    elif number < 0:
        print("Invalid input. Please enter a positive number greater than 0.")
        continue
    else:
        for i in range(1, number + 1):
            for j in range(number - i):
                print(" ", end="")
            for k in range(2 * i - 1):
                print("*", end="")
            print()

# END
