# HOMEWORK LESSON 5 TARGIL 3 PART A


# nested loop exercise
# input from user a positive number bigger than 0
# print the next cimetrical shape
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1


# START

number = int(input("Enter a positive number greater than 0: "))

if number <= 0:
    print("Invalid input. Please enter a positive number greater than 0.")
else:
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    for i in range(number - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()



# END


# Enter a positive number greater than 0: 5
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1