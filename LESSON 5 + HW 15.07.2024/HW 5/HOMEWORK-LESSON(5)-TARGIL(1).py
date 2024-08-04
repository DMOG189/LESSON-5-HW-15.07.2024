# HOMEWORK LESSON 5 TARGIL 1

# input 10 numbers from user
# print
# a. how many positive numbers
# b. how many negative numbers
# c. how many times the number 0 has been mentioned
# d.how many numbers devide in 7 with no remain
# e. what was the last positive number, if there was none print none
# f. what was the last negative number, if there was none print none
# g. if entered a number bigger than 1000 or smaller than -1000 ignore with continue
# h. if entered the number -9999 exit the loop and don't print statistics at all

# USE ELSE LOOP LIKE LEARNED IN CLASS !!!

# START

positive_count = 0
negative_count = 0
zero_count = 0
divisible_by_7_count = 0
last_positive = None
last_negative = None

for _ in range(10):
    num = int(input("Enter a number: "))

    if num == -9999:
        print("Exiting the loop and not printing statistics.")
        break

    if num > 1000 or num < -1000:
        continue

    if num > 0:
        positive_count += 1
        last_positive = num
    elif num < 0:
        negative_count += 1
        last_negative = num
    else:
        zero_count += 1

    if num % 7 == 0:
        divisible_by_7_count += 1
else:
    print(f"Number of positive numbers: {positive_count}")
    print(f"Number of negative numbers: {negative_count}")
    print(f"Number of times 0 was mentioned: {zero_count}")
    print(f"Number of numbers divisible by 7 with no remainder: {divisible_by_7_count}")
    print(f"Last positive number: {last_positive if last_positive is not None else 'None'}")
    print(f"Last negative number: {last_negative if last_negative is not None else 'None'}")


# END