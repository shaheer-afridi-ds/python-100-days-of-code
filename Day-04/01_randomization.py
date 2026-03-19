#have to use or have to import random libraries to use random module
import random

#for integer
random_integer = random.randint(1, 10)
print(random_integer)

#for float if u want to expand it * it by number
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

#if u want to give ur own number to randomize in between
random_float = random.uniform(1, 10)
print(random_float)

#random head or tails program
random_head_tail = random.randint(0,2)
if random_head_tail == 0:
    print("Heads")
else:
    print("Tails")
