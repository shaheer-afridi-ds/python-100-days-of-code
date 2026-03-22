# Day 6 - While Loops

# what is while loop?
# while loop runs again and again while condition is true

# simple example
count = 1

while count <= 3:
    print("Count is:", count)
    count += 1


# -----------------------------------
# Hurdle Challenge using while loop
# -----------------------------------

# function to jump over hurdle
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# using while loop
# here we use front_is_clear() from reeborg

while not at_goal():
    move()
    jump()
