# LESSON 5 EX 8 NESTED LOOP TARGIL 4

# input number from user, i.e. 5
# 1
# 12
# 123
# 1234
# 12345



# START

number = int(input("Enter a number: "))


for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# END

# Enter a number: 5
# 1
# 12
# 123
# 1234
# 12345
