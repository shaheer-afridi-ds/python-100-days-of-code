# Day 6 - Functions

# what is def?
# def is a keyword used to create (define) a function
# function is a block of code that runs when we call it

# -----------------------------
# Built-in Functions (already made by python)
# -----------------------------

print("This is built-in function")   # print() is built-in

name = input("Enter your name: ")   # input() is built-in
length = len(name)                 # len() is built-in

print("Your name has", length, "letters")


# -----------------------------
# User-defined Functions (we create them)
# -----------------------------

# simple function
def greet():
    print("Hello!")
    print("Welcome to Day 6")

# calling the function
greet()


# function with input
def greet_user():
    name = input("What is your name? ")
    print("Hello " + name)

greet_user()


# function for addition
def add_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = num1 + num2
    print("Sum is:", total)

add_numbers()


# another simple function
def say_bye():
    print("Okay bye!")

say_bye()
