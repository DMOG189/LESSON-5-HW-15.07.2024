# lesson 5 ex 4 CONTINUE TARGIL 3

# input numbers from the user
# print the max number of the input
# exit the loop when you at least have 10 numbers
# ignore minus numbers

# do the same with a minimum

# START

number: int = 0;
the_max: int = None;
the_min: int = None;

while True:
    number = int(input("Enter number [-999 to exit]:"))
    if number == -999:
        break;

# WAY 1

    if the_min == None or number < the_min:
        the_min = number;

# WAY 2

    if not the_min or number < the_min:
        the_min = number;

# WAY 3

    the_min = number if not the_min or number < the_min else the_min;

print(f"the min number is {the_min}");
print(f"the max number is {the_max}");

# END