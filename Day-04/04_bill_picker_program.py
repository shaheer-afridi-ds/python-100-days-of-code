# Day 04 - Table Roulette (Who Pays the Bill)

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Method 1: Using randint with if-elif
random_banker = random.randint(0, 4)

if random_banker == 0:
    print("Alice")
elif random_banker == 1:
    print("Bob")
elif random_banker == 2:
    print("Charlie")
elif random_banker == 3:
    print("David")
else:
    print("Emanuel")

# Method 2: Using random.choice()
print(random.choice(friends))

# Method 3: Using random index
random_index = random.randint(0, 4)
print(friends[random_index])
