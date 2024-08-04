# lesson 5 ex 2 CONTINUE TARGIL 2

# input numbers from the user
# print the max number of the input
# exit the loop when you at least have 10 numbers
# ignore minus numbers


# START

number: int = 0
count: int = 0
the_max: int = None

while True:
    number = int(input("Enter a number:"));
    if number == -999:
        break
    if number < 0:
        continue
    if not the_max or number > the_max:
        the_max = number
    count += 1
    if count >= 10:
        break

    # WAY 1
    if the_max == None or number > the_max:
        the_max = number

    # WAY 2
    if not the_max or number > the_max:
        the_max = number

    # WAY 3
    the_max = number if not the_max or number > the_max else the_max;


print(f"the max number is {the_max}");


# END