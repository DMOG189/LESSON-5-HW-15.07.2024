# HOMEWORK LESSON 5 TARGIL 4


# START

# PART A:
# make a list of str inside put 3 favorite songs
# now add another song to the list using append
# now add another song to the start of the list using insert
# print the list length using len

favorite_songs = ["BESAME", "TIMES MOVES SLOW", "CHOP SUEY"]
favorite_songs.append("HOTEL CALIFORNIA")
favorite_songs.insert(0, "TUYO")
print(f"The list of favorite songs: {favorite_songs}")
print(f"Length of the list: {len(favorite_songs)}")

# END


# START

# PART B:
# make a list of full numbers int
# and randomize 10 different number in it
# using for loop randint and append

import random

numbers = []

for _ in range(10):
    num = random.randint(1, 100)
    numbers.append(num)

print(f"The list of random numbers: {numbers}")

# END



# START

# PART C:
# make a list of bool and randomize it with 10 random values
# each one can be either True or False
# using for loop, random.choice, append

# import random

bool_list = []

for _ in range(10):
    value = random.choice([True, False])
    bool_list.append(value)

print(f"The list of random boolean values: {bool_list}")

# END