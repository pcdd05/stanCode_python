from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: DiCheng
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    pre-cond: Karel is at (st.1, ave.1), facing East and ready to paint checkerboard.
    post-cond: Karel had painted a beautiful checkerboard.
    """
    check_the_checkerboard()
    while front_is_clear():
        linear_put_beeper()
        check_previous_spot()
        up_one_street()


def check_the_checkerboard():
    """
    Find out what kind of checkerboard where Karel at, horizontal or vertical or 1x1 jail.
    """
    if not front_is_clear():
        turn_north()
    if not front_is_clear():
        put_beeper()


def linear_put_beeper():
    """
    Karel is moving linearly, put beeper in every 2 moves.
    """
    put_beeper()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        for i in range(2):
            if front_is_clear():
                move()


def check_previous_spot():
    """
    Karel will check previous spot in the end of line to decide whether end up with beeper or not.
    """
    turn_around()
    if front_is_clear():
        move()
        if on_beeper():
            turn_around()
            move()
        else:
            turn_around()
            move()
            put_beeper()


def up_one_street():
    """
    Karel will climb up 1 street and turn to horizontal direction.
    """
    turn_north()
    if front_is_clear():
        # decide the start position of next street.
        if on_beeper():
            move()
            turn_to_horizontal()
            move()
        else:
            move()
            turn_to_horizontal()


def turn_to_horizontal():
    """
    Check positions and make turn for next round.
    """
    if left_is_clear():
        turn_left()
    else:
        turn_right()


def turn_north():
    """
    Karel will turn to North side.
    """
    while not facing_north():
        turn_left()


def turn_around():
    """
    Karel will turn around.
    """
    for i in range(2):
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