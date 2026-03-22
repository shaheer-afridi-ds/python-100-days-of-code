# Day 6 - Indentation in Python

# what is indentation?
# indentation means giving spaces at the beginning of a line
# python uses indentation to understand blocks of code

# example 1 (correct indentation)
if 5 > 2:
    print("5 is greater than 2")


# example 2 (wrong indentation - will give error)
# if 5 > 2:
# print("This will cause error")


# indentation in functions
def greet():
    print("Hello")
    print("How are you?")

greet()


# indentation in loops
for i in range(3):
    print("Hello", i)


# nested indentation
if True:
    print("Level 1")
    if True:
        print("Level 2")
