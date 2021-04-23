from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: DiCheng
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    pre-cond: Karel is at (st.1, ave.1), facing East, while some of columns need to be fixed.
    post-cond: Karel is at (st.1, last ave.), facing East, while every columns are fixed and solid.
    """
    while front_is_clear():
        horizontal_check_and_fix()
        up_one_street()
    back_down()


def horizontal_check_and_fix():
    """
    Karel is moving horizontal, checking and fixing columns in every 4 moves.
    """
    while front_is_clear():
        check_and_put_beeper()
        # move to the next column.
        for i in range(4):
            move()
    check_and_put_beeper()


def check_and_put_beeper():
    """
    put beeper if not on beeper.
    """
    if not on_beeper():
        put_beeper()


def up_one_street():
    """
    Karel will facing north first and then climb up 1 street, end up with turn into horizontal directions.
    """
    # turn north first.
    turn_north()
    # check if not on the top then climb up.
    if front_is_clear():
        move()
        # check positions and make turn for next round.
        if left_is_clear():
            turn_left()
        else:
            turn_right()


def back_down():
    """
    Karel will climb down to (st.1, last ave.), facing East.
    """
    turn_south()
    while front_is_clear():
        move()
    turn_east()


def turn_north():
    """
    Karel will turn to North side.
    """
    while not facing_north():
        turn_left()


def turn_south():
    """
    Karel will turn to South side.
    """
    while not facing_south():
        turn_left()


def turn_east():
    """
    Karel will turn to East side.
    """
    while not facing_east():
        turn_left()


def turn_right():
    """
    Karel will turn right.
    """
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
