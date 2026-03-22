# Day 6 - Hurdle with Variable Heights

# in this challenge hurdles are not same height
# so robot needs to keep going up until path is clear

# function to turn right (because not built-in in reeborg)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# function to jump over different height hurdles
def jump():
    # go up until no wall on right
    turn_left()
    while wall_on_right():
        move()

    # cross the hurdle
    turn_right()
    move()
    turn_right()

    # come down until ground
    while front_is_clear():
        move()

    turn_left()

# main loop
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
