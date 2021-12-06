def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()
    turn_right()
    move()
    
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        jump()