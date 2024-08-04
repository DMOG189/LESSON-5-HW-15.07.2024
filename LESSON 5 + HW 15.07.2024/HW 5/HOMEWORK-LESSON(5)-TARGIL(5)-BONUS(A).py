# HOMEWORK LESSON 5 TARGIL 5 BONUS A

# BONUS
# create a random word using a, b, c
# shuffle a word length between 5-20
# shuffle a letter from a, b, c until you get a word


# START

import random

letters = ['a', 'b', 'c']
word_length = random.randint(5, 20)
random_word = ''.join(random.choice(letters) for _ in range(word_length))

print(f"The random word is: {random_word}")

# END

# The random word is: aacbccc