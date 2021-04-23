"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE:
KEEP THE ENGINE ON AND ON WHILE ALWAYS TRUE!
"""

from campy.gui.events.timer import pause
from SC101_Assignment2_鄭迪.breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics(num_lives=NUM_LIVES)

    while True:
        # page 1, 3, 4 animation loop
        if graphics.get_page_no() == 1 or graphics.get_page_no() == 3 or graphics.get_page_no() == 4:
            # update
            graphics.get_ball().move(graphics.get_ball().get_dx(), graphics.get_ball().get_dy())
            graphics.paddle_follow_ball()
            # check
            if graphics.get_ball().x <= 0 or graphics.get_ball().x + graphics.get_ball().width > graphics.get_window().width:
                graphics.get_ball().bounce_dx()
                graphics.change_random_color()
            if graphics.get_ball().y <= 0 or graphics.background_ball_hit_something():
                graphics.get_ball().bounce_dy()
                graphics.change_random_color()
        # page 2(main game) animation loop
        elif graphics.get_page_no() == 2:
            if graphics.get_life_point() > 0:
                if graphics.get_game_on():
                    # update
                    if graphics.get_ball() is not None:
                        graphics.get_ball().move(graphics.get_ball().get_dx(), graphics.get_ball().get_dy())
                    if graphics.get_have_extra_ball():
                        graphics.get_extra_ball().move(graphics.get_extra_ball().get_dx(), graphics.get_extra_ball().get_dy())
                    if graphics.get_effect_ball_show():
                        graphics.get_effect_ball().move(0, graphics.get_effect_ball().get_dy())
                        graphics.get_effect_ball().get_effect_label().move(0, graphics.get_effect_ball().get_dy())
                    # check
                    # check extra ball
                    if graphics.get_have_extra_ball():
                        if graphics.get_extra_ball().x <= 0 or graphics.get_extra_ball().x + graphics.get_extra_ball().width > graphics.get_window().width:
                            graphics.get_extra_ball().bounce_dx()
                        if graphics.get_extra_ball().y <= 0 or graphics.extra_ball_hit_something() or (graphics.get_brick_nums() == 0 and graphics.get_extra_ball().y + graphics.get_extra_ball().height > graphics.get_window().height):
                            graphics.get_extra_ball().bounce_dy()
                        if graphics.get_extra_ball().y > graphics.get_window().height:
                            graphics.set_ball_count(-1)
                            graphics.remove_extra_ball()
                    # check ball
                    if graphics.get_ball() is not None:
                        if graphics.get_ball().x <= 0 or graphics.get_ball().x + graphics.get_ball().width > graphics.get_window().width:
                            graphics.get_ball().bounce_dx()
                        if graphics.get_ball().y <= 0 or graphics.ball_hit_something() or (graphics.get_brick_nums() == 0 and graphics.get_ball().y + graphics.get_ball().height > graphics.get_window().height):
                            graphics.get_ball().bounce_dy()
                    if (not graphics.get_have_extra_ball() and graphics.get_ball_count() == 1) or (graphics.get_have_extra_ball() and graphics.get_ball_count() > 1):
                        if graphics.get_ball().y > graphics.get_window().height:
                            graphics.set_ball_count(-1)
                            graphics.remove_ball()
                    # check life point
                    if graphics.get_ball_count() == 0:
                        graphics.set_life_point(-1)
                        graphics.update_life_point()
                        if graphics.get_life_point() > 0:
                            graphics.one_more_chance()
                        else:
                            graphics.game_over()
                    # check effect ball
                    if graphics.get_effect_ball_show():
                        graphics.check_effect_ball_hit_paddle()
                        if graphics.get_effect_ball().y > graphics.get_window().height:
                            graphics.get_window().remove(graphics.get_effect_ball().get_effect_label())
                            graphics.get_window().remove(graphics.get_effect_ball())
                            graphics.set_effect_ball_show(False)
                            graphics.set_effect_ball_desc("")
                    # check effect time
                    if graphics.get_effecting():
                        graphics.check_effect_time()

        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
