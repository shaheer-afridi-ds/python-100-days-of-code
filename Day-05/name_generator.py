import random

adjectives = ['Cool', 'Crazy', 'Dark', 'Silent', 'Fierce', 'Shadow', 'Flying', 'Wild', 'Epic', 'Swift']
nouns = ['Tiger', 'Ninja', 'Dragon', 'King', 'Shadow', 'Wolf', 'Falcon', 'Knight', 'Hunter', 'Wizard']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print('Hi! Welcome to Python Name Generator Program!')

nr_adjective = int(input("How many adjectives do you want?\n"))
nr_nouns = int(input("How many nouns do you want?\n"))
nr_numbers = int(input("How many numbers do you want?\n"))

name_list = []

for _ in range(nr_adjective):
    name_list.append(random.choice(adjectives))

for _ in range(nr_nouns):
    name_list.append(random.choice(nouns))

for _ in range(nr_numbers):
    name_list.append(random.choice(numbers))

random.shuffle(name_list)

name = ""
for char in name_list:
    name += char

print(f"Your name is: {name}")
