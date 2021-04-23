"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE:
CLASSIC AND GREAT, INSPIRING A LOT.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

RED_R = 255            # Red Color RGB
RED_G = 0              # Red Color RGB
RED_B = 0              # Red Color RGB

ORANGE_R = 255         # Orange Color RGB
ORANGE_G = 165         # Orange Color RGB
ORANGE_B = 0           # Orange Color RGB

YELLOW_R = 255         # Yellow Color RGB
YELLOW_G = 255         # Yellow Color RGB
YELLOW_B = 0           # Yellow Color RGB

GREEN_R = 0            # Green Color RGB
GREEN_G = 255          # Green Color RGB
GREEN_B = 0            # Green Color RGB

BLUE_R = 0             # Blue Color RGB
BLUE_G = 0             # Blue Color RGB
BLUE_B = 255           # Blue Color RGB


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.__window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.__window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.__window = GWindow(width=self.__window_width, height=self.__window_height, title=title)

        # Create a paddle
        self.__paddle = GRect(paddle_width, paddle_height)
        self.__paddle.filled = True
        self.__window.add(self.__paddle, self.__window.width / 2 - self.__paddle.width / 2, self.__window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.__ball = GOval(ball_radius * 2, ball_radius * 2)
        self.__ball.filled = True
        self.__window.add(self.__ball, self.__window.width / 2 - self.__ball.width / 2, self.__window.height / 2 + self.__ball.height / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.__restart_game = False
        self.__game_start = False
        onmouseclicked(self.click_event)
        onmousemoved(self.move_event)

        # Draw bricks
        self.__brick_rows = brick_rows
        self.__brick_cols = brick_cols
        self.__brick_width = brick_width
        self.__brick_height = brick_height
        self.__brick_spacing = brick_spacing
        self.__brick_offset = brick_offset
        self.__brick_nums = 0
        self.set_bricks(self.__brick_rows, self.__brick_cols, self.__brick_width, self.__brick_height, self.__brick_spacing, self.__brick_offset)

        # Prepare label
        self.__score = 0
        self.__top_score = 0
        self.__game_end_label = GLabel("GAME OVER")
        self.__game_end_label.font = "Verdana-17"
        self.__game_end_label.color = (150, 0, 0)
        self.__score_label = GLabel("Your Score : " + str(self.__score))
        self.__score_label.font = "Verdana-15"
        self.__score_label.color = (100, 100, 100)
        self.__top_score_label = GLabel("Top Score : " + str(self.__top_score))
        self.__top_score_label.font = "Verdana-15"
        self.__top_score_label.color = (100, 100, 100)
        self.__hint_label = GLabel("Click to Start")
        self.__hint_label.font = "Verdana-15"
        self.__hint_label.color = (100, 100, 100)
        self.__window.add(self.__game_end_label, self.__window.width / 2 - self.__game_end_label.width / 2, 0)
        self.__window.add(self.__score_label, 0, self.__score_label.height)
        self.__window.add(self.__top_score_label, self.__window.width - self.__top_score_label.width, self.__top_score_label.height)
        self.__window.add(self.__hint_label, self.__window.width / 2 - self.__hint_label.width / 2, self.__window.height / 2 + self.__ball.height / 2 + self.__ball.height + self.__hint_label.height * 4)
        self.__life_point_text = ""
        for i in range(3):
            self.__life_point_text += "❤"
        self.__life_point_label = GLabel(self.__life_point_text)
        self.__life_point_label.font = "-22"
        self.__life_point_label.color = (150, 0, 0)
        self.__window.add(self.__life_point_label, self.__window.width - self.__life_point_label.width, self.__window.height)

    def set_bricks(self, brick_rows, brick_cols, brick_width, brick_height, brick_spacing, brick_offset):
        """
        Setting the bricks depends on the brick_rows and brick_cols.
        """
        for x in range(brick_rows):
            for y in range(brick_cols):
                __brick = GRect(brick_width, brick_height)
                __brick.filled = True
                if y < 2:
                    __brick.fill_color = (RED_R, RED_G, RED_B)
                elif y < 4:
                    __brick.fill_color = (ORANGE_R, ORANGE_G, ORANGE_B)
                elif y < 6:
                    __brick.fill_color = (YELLOW_R, YELLOW_G, YELLOW_B)
                elif y < 8:
                    __brick.fill_color = (GREEN_R, GREEN_G, GREEN_B)
                else:
                    __brick.fill_color = (BLUE_R, BLUE_G, BLUE_B)
                __brick.color = (0, 0, 0)
                # if y == 9: (This line switch for building only one row of bricks.)
                #     self.__window.add(__brick, x * (brick_width + brick_spacing), brick_offset + y * (brick_height + brick_spacing))
                #     self.__brick_nums += 1
                self.__window.add(__brick, x * (brick_width + brick_spacing), brick_offset + y * (brick_height + brick_spacing))
                self.__brick_nums += 1


    def refill_bricks(self):
        """
        Refill the bricks when game restart.
        """
        for x in range(self.__brick_rows):
            for y in range(self.__brick_cols):
                __x_coordinate = x * (self.__brick_width + self.__brick_spacing)
                __y_coordinate = self.__brick_offset + y * (self.__brick_height + self.__brick_spacing)
                if self.__window.get_object_at(__x_coordinate, __y_coordinate) is None:
                    __brick = GRect(self.__brick_width, self.__brick_height)
                    __brick.filled = True
                    if y < 2:
                        __brick.fill_color = (RED_R, RED_G, RED_B)
                    elif y < 4:
                        __brick.fill_color = (ORANGE_R, ORANGE_G, ORANGE_B)
                    elif y < 6:
                        __brick.fill_color = (YELLOW_R, YELLOW_G, YELLOW_B)
                    elif y < 8:
                        __brick.fill_color = (GREEN_R, GREEN_G, GREEN_B)
                    else:
                        __brick.fill_color = (BLUE_R, BLUE_G, BLUE_B)
                    __brick.color = (0, 0, 0)
                    # if y == 9: (This line switch for building only one row of bricks.)
                    #     self.__window.add(__brick, __x_coordinate, __y_coordinate)
                    #     self.__brick_nums += 1
                    self.__window.add(__brick, __x_coordinate, __y_coordinate)
                    self.__brick_nums += 1

    def click_event(self, mouse_obj):
        """
        Setting events when mouse clicked on different pages/conditions.
        """
        if self.__restart_game:
            self.clean_record()
            self.set_ball_position()
            self.__game_end_label.y = 0
            self.refill_bricks()
            self.update_life_point(3)
            self.__restart_game = False
        elif not self.__game_start:
            self.__game_start = True
            self.__hint_label.y = 0
            self.initial_velocity()

    def move_event(self, mouse_obj):
        """
        Setting events when mouse moved on different pages/conditions.
        """
        if mouse_obj.x <= 0:
            self.__paddle.x = 0
        elif mouse_obj.x + self.__paddle.width >= self.__window_width:
            self.__paddle.x = self.__window_width - self.__paddle.width
        else:
            self.__paddle.x = mouse_obj.x

    def initial_velocity(self):
        """
        initial the velocity to make ball move.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def set_ball_position(self):
        """
        Set ball's position to the default on center of screen.
        """
        self.__dx = 0
        self.__dy = 0
        self.__ball.x = self.__window.width / 2 - self.__ball.width / 2
        self.__ball.y = self.__window.height / 2 + self.__ball.height / 2

    def one_more_chance(self):
        """
        When losing one life point but still have chances to challenge.
        """
        self.set_ball_position()
        self.__hint_label.text = "Click to Start"
        self.__hint_label.y = self.__window.height / 2 + self.__ball.height / 2 + self.__ball.height + self.__hint_label.height * 4
        self.update_score()
        self.__game_start = False

    def game_over(self):
        """
        When losing all life then game over.
        """
        self.__dx = 0
        self.__dy = 0
        self.__game_end_label.text = "GAME OVER"
        self.__game_end_label.y = self.__window.height / 2 + self.__ball.height / 2 - self.__game_end_label.height
        self.__score_label.text = "Your Score : " + str(self.__score)
        self.__hint_label.text = "Click to Restart"
        self.__hint_label.y = self.__window.height / 2 + self.__ball.height / 2 + self.__ball.height + self.__hint_label.height * 4
        self.update_score()

        self.__game_start = False
        self.__restart_game = True

    def update_score(self):
        """
        Update the current score and top score.
        """
        if self.__score > self.__top_score:
            self.__top_score = self.__score
        self.__score_label.text = "Your Score : " + str(self.__score)
        self.__top_score_label.text = "Top Score : " + str(self.__top_score)
        self.__top_score_label.x = self.__window.width - self.__top_score_label.width

    def clean_record(self):
        """
        Reset the scores record.
        """
        self.__score = 0

    def hit_something(self):
        """
        For ball on screen detecting is hitting something or not.
        """
        for x in range(2):
            for y in range(2):
                maybe_hit_obj = self.__window.get_object_at(self.__ball.x + x * 2 * BALL_RADIUS, self.__ball.y + y * 2 * BALL_RADIUS)
                if maybe_hit_obj is None or maybe_hit_obj is self.__game_end_label or maybe_hit_obj is self.__score_label or maybe_hit_obj is self.__top_score_label or maybe_hit_obj is self.__life_point_label or maybe_hit_obj is self.__hint_label:
                    pass
                else:
                    # when hit bricks
                    if maybe_hit_obj.y < self.__paddle.y:
                        self.__window.remove(maybe_hit_obj)
                        self.__score += 1
                        self.__brick_nums -= 1
                        self.update_score()
                        self.all_bricks_clear()
                    # when hit paddle, prevent loop in +-dy
                    if maybe_hit_obj.y >= self.__paddle.y and self.__dy < 0:
                        return False
                    return True

    def all_bricks_clear(self):
        """
        Check the is all bricks are down to decide if it's game clear.
        """
        if self.__brick_nums == 0:
            self.update_score()
            self.__game_end_label.color = (0, 0, 150)
            self.__game_end_label.text = "GAME CLEAR"
            self.__game_end_label.y = self.__window.height / 2 + self.__ball.height / 2 - self.__game_end_label.height
            self.__hint_label.text = "Click to Restart"
            self.__hint_label.y = self.__window.height / 2 + self.__ball.height / 2 + self.__ball.height + self.__hint_label.height * 4
            self.__game_start = False
            self.__restart_game = True
            return True

    def get_window(self):
        """
        Return the GWindow in use.
        """
        return self.__window

    def get_paddle(self):
        """
        Return the paddle.
        """
        return self.__paddle

    def get_ball(self):
        """
        Return the ball.
        """
        return self.__ball

    def get_dx(self):
        """
        Return the ball's x-pace.
        """
        return self.__dx

    def set_dx(self, dx):
        """
        Set the ball's x-pace.
        """
        self.__dx = dx

    def get_dy(self):
        """
        Return the ball's y-pace.
        """
        return self.__dy

    def set_dy(self, dy):
        """
        Set the ball's y-pace.
        """
        self.__dy = dy

    def update_life_point(self, life_point):
        """
        Update current life point left.
        """
        self.__life_point_text = ""
        for i in range(life_point):
            self.__life_point_text += "❤"
        self.__life_point_label.text = self.__life_point_text

