"""
File: bouncing_ball.py
Name: DiCheng
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval, GLabel, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked, onmousemoved

# This constant controls the x velocity.
VX = 3
# This constant controls the pause per ms between each movement.
DELAY = 10
# This constant controls the increase or decrease amount of y velocity in each movement.
GRAVITY = 1
# This constant controls the size of the ball and the font size of restart_button.
SIZE = 20
# This constant controls the decrease y velocity when each bounce up.
REDUCE = 0.9
# This constant controls the start position of x-coordinate.
START_X = 30
# This constant controls the start position of y-coordinate.
START_Y = 40
# This constant represent for color black.
BLACK = "black"
# This constant represent for color red.
RED = "red"
# This global variable create a GWindow instance.
window = GWindow(800, 500, title='bouncing_ball.py')
# This global variable create a GOval instance.
ball = GOval(SIZE, SIZE)
# This global variable controls mouse click is disabled or not.
click_disabled = False
# This global variable controls the total bouncing times under 3 times.
count = 0

# extension: This global variable create a GLabel instance for showing restart button.
restart_button = GLabel("Click To Restart")
# extension: Set attribute to restart_button font at global zone is for button_frame referring to the size.
restart_button.font = "Verdana-" + str(SIZE)
# extension: This global variable create a GRect instance for making a frame for button.
button_frame = GRect(restart_button.width*1.2, restart_button.height*1.2)


def main():
    """
    This program will set attribute to the ball and add ball instance on window,
    while listening to onmouseclicked and onmousemoved events.
    """
    ball_setting()
    onmouseclicked(click_event)
    onmousemoved(move_event)


def ball_setting():
    ball.color = BLACK
    ball.filled = True
    ball.filled_color = BLACK
    window.add(ball, START_X, START_Y)


def click_event(mouse_obj):
    """
    When user click mouse,
    depends on whether is click on restart button or not, functions will do ball_bouncing or do restart.
    :param mouse_obj: class, a GMouseEvent instance to indicate where the user's mouse is.
    """
    if window.get_object_at(mouse_obj.x, mouse_obj.y) is not restart_button:
        ball_bouncing()
    else:
        restart()


def ball_bouncing():
    """
    Depends on the click_disabled and ball bouncing times count to decide whether do bouncing or do nothing.
    """
    global click_disabled, count
    if not click_disabled and count < 3:
        count += 1
        click_disabled = True
        vy = 0
        while click_disabled:
            vy += GRAVITY
            ball.move(VX, vy)
            # bounce when ball touch the ground.
            if vy > 0 and ball.y + ball.height >= window.height:
                vy *= -REDUCE
            # when ball bounce out of window, unlock mouse click and show restart button if already had bounced 3 times.
            if ball.x > window.width:
                click_disabled = False
                if count >= 3:
                    show_restart_button()
            pause(DELAY)
        ball.x = START_X
        ball.y = START_Y


def show_restart_button():
    """
    extension:
    adding restart_button and button_frame instances to window.
    """
    button_frame.color = BLACK
    window.add(button_frame, (window.width - button_frame.width)/2, (window.height - button_frame.height)/2)
    window.add(restart_button, (window.width - restart_button.width)/2, (window.height - restart_button.height)/2 + restart_button.height)


def restart():
    """
    extension:
    When click restart button, do reset the bouncing count and remove restart button to bounce again.
    """
    global count
    count = 0
    window.remove(restart_button)
    window.remove(button_frame)
    ball_bouncing()


def move_event(mouse_obj):
    """
    extension:
    When user move mouse,
    this function will get the mouse coordinate and set attribute of color to both restart_button and button_frame.
    :param mouse_obj: class, a GMouseEvent instance to indicate where the user's mouse is.
    """
    if window.get_object_at(mouse_obj.x, mouse_obj.y) is restart_button:
        button_frame.color = RED
        restart_button.color = RED
    elif restart_button.color != ball.color:
        button_frame.color = BLACK
        restart_button.color = BLACK


if __name__ == "__main__":
    main()
