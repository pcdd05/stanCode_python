from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: DiCheng
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    pre-cond: Karel is at (street 4, avenue 3) in the wall zone, facing East;
              1 beeper is at (st.3, ave.6) in front of the gate.
    post-cond: Karel is at (st.4, ave.3) in the wall zone, facing East;
               1 beeper is at (st.4, ave.3).
    """
    move_to_the_beeper()
    pick_beeper()
    back_to_original_spot()
    put_beeper()


def move_to_the_beeper():
    """
    pre-cond: Karel is at (street 4, avenue 3) in the wall zone, facing East;
              1 beeper is at (st.3, ave.6) in front of the gate.
    post-cond: Karel is at (st.3, ave.6) in front of the gate, facing East;
               1 beeper is at (st.3, ave.6).
    """
    move_to_the_end()
    turn_right()
    move_to_the_gate()
    while not on_beeper():
        move()


def move_to_the_end():
    """
    Karel will move forward till in front of the wall.
    """
    while front_is_clear():
        move()


def move_to_the_gate():
    """
    Karel will move to the gate, facing outside the gate.
    """
    while not left_is_clear():
        move()
    turn_left()


def back_to_original_spot():
    """
    pre-cond: Karel is at (st.3, ave.6) in front of the gate, facing East.
    post-cond: Karel is at (st.4, ave.3) in the wall zone, facing East;
               1 beeper is at (st.4, ave.3).
    """
    turn_around()
    move_to_the_end()
    turn_right()
    move_to_the_end()
    turn_right()


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
