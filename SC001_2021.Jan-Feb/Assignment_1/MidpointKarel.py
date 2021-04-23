from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: DiCheng
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    pre-cond: Karel is at (st.1, ave.1), facing East and ready to find the middle of the street.
    post-cond: Karel is at the middle of the street, facing North as hooray!
    """
    set_up_beeper_wall()
    shrink_beeper_wall_till_middle_point()
    hooray_in_the_middle()


def set_up_beeper_wall():
    """
    Karel using beeper to set the boundary as a wall.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()


def shrink_beeper_wall_till_middle_point():
    """
    Karel move back and forward to shrink the boundary wall till the middle point.
    """
    turn_around()
    pick_beeper()
    if front_is_clear():
        move()
        if not on_beeper():
            put_beeper()
            move_to_the_other_beeper_wall()


def move_to_the_other_beeper_wall():
    """
    Karel move forward to find the other boundary wall and keep shrinking.
    """
    if front_is_clear():
        move()
        while not on_beeper():
            move()
        shrink_beeper_wall_till_middle_point()


def hooray_in_the_middle():
    """
    Karel facing North as hooray in the middle!
    """
    while not facing_north():
        turn_left()


def turn_around():
    """
    Make Karel turn around.
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
