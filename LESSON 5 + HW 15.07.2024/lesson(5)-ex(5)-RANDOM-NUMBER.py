# LESSON 5 EX 5

# IMPORT / RANDOM

# print 30 rendom numbers between 1 - 45

# START

# import (brings module into program)
import random

for i in range(1, 7):
   rnd: int = random.randint(1, 45)
   print(rnd, end=" ");

# nosaf

nosaf: int = random.randint(1, 6)
print(f"mispar nosaf = {nosaf}");


# END


random_bool: bool = random.choice([True , False])
random_name: str = random.choice(["danny", "yoysi", "shloimale"])
# 10 * random.random() # 0.0 -- 1.0
