# Day 6 - Hurdle Loop Challenge

# in this challenge we make the robot jump over hurdles again and again

# function to make robot jump
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# using loop to repeat jumping
for step in range(6):   # number depends on hurdles
    move()
    jump()
