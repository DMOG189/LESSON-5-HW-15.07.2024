# lesson 5 ex 1 CONTINUE

# START

# input grades from user
# until got grade 999
# if user misritten a grade
# that is not between 0 - 100
# then ignore

# NO CONTINUE

grade: int = 0;
the_sum: int = 0;
count: int = 0;

while True:
    grade = int(input("Enter Grade:"));
    if grade == 999:
        break
    if grade < 0 or > 100:
        the_sum += grade
        count += 1;

print(f"the avg is {the_sum / count: .2f}");


# CONTINUE

grade: int = 0;
the_sum: int = 0;
count: int = 0;

while True:
    grade = int(input("Enter Grade:"));
    if grade == 999:
        break
    if grade < 0 or grade > 100:
        continue
    the_sum += grade
    count += 1;

print(f"the avg is {the_sum / count: .2f}");

# END
