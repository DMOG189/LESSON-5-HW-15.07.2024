# HOMEWORK LESSON 5 TARGIL 5 BONUS B

# BONUS B
# create a random word using a, b, c
# shuffle a word length between 5-20
# shuffle a letter from a, b, c until you get a word
# improve the solution
# create a list that holds a random number of words
# every word would be random
# shuffle a list length between 10-20 words
# fill the list with random words for the shuffled length
# example: if were shuffled 12 different words the list will include 12 random words


# START

import random

def generate_random_word():
    letters = ['a', 'b', 'c']
    word_length = random.randint(5, 20)
    return ''.join(random.choice(letters) for _ in range(word_length))

list_length = random.randint(10, 20)
random_words_list = [generate_random_word() for _ in range(list_length)]

print(f"The list of {list_length} random words is: {random_words_list}")

# END