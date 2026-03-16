# Day1: Variables + Inputs Exercises
# doing the course by Angela’s Python

name = input("What is your name?\n")
print("Hello " + name + "!")

# 2️Favorite color
color = input("What is your favorite color?\n")
print("Wow! " + color + " is a beautiful color!")

# 3️⃣ Favorite food
food = input("What is your favorite food?\n")
print("Yum! I love " + food + " too!")

# 4️⃣ Check the length of user input in 1 line this also comes in string manipulation
print(len(input("Enter your name to check its length:\n")))

# 5️⃣ Split into variables
username = input("Enter your name again:\n")  # store input in a variable
length = len(username)                        # calculate length using the variable
print("The length of your name is:", length)  # print length
