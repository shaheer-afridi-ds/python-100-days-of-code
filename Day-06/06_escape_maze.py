# Day 6 - Escape the Maze
# Using loops, functions, and logic to reach the goal

# function to turn right (not built-in)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# function to move along walls
def move_forward():
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()

# function to follow maze path
def follow_right_wall():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# main loop to escape maze
while not at_goal():
    follow_right_wall()
