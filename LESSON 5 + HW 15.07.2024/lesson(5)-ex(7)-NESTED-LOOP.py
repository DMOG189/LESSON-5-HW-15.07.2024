# LESSON 5 EX 7 NESTED LOOP EXAMPLE

# nested loop is a loop inside a loop


# START

number: int = 1

for j in range(1, 4):
    for i in range(1, 6):
        for k in range(1, 6):
            print(i, end=" ")
            number += 1
    print()


# END

# 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5
# 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5
# 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5