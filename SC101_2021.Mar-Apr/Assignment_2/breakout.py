"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE:
THIS IS THE ORIGINAL MODEL OF ALL.
"""

from campy.gui.events.timer import pause
from SC101_Assignment2_鄭迪.breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES
    graphics.update_life_point(num_lives)

    while True:
        if num_lives > 0:
            # update
            graphics.get_ball().move(graphics.get_dx(), graphics.get_dy())
            # check
            if graphics.get_ball().x <= 0 or graphics.get_ball().x + graphics.get_ball().width > graphics.get_window().width:
                graphics.set_dx(-graphics.get_dx())
            if graphics.get_ball().y <= 0 or graphics.hit_something() or (graphics.get_ball().y + graphics.get_ball().height > graphics.get_window().height and graphics.all_bricks_clear()):
                graphics.set_dy(-graphics.get_dy())
            if graphics.get_ball().y > graphics.get_window().height:
                num_lives -= 1
                graphics.one_more_chance()
                graphics.update_life_point(num_lives)
            if graphics.all_bricks_clear():
                num_lives = NUM_LIVES
        else:
            graphics.game_over()
            num_lives = NUM_LIVES
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
