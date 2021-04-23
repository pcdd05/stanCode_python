"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE:
I WANNA PLAY A GOOD GAME!
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from datetime import date

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
EFFECT_BALL_SIZE = 15  # size of the effect ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3          # Number of attempts
DEFAULT_BRICK_LVL_LST = [[5, 6, 8, 9, 10], [3, 4, 7], [1, 2]]    # Default bricks color type in row number grouped.
DEFAULT_THEME_R = 0    # Default theme color RGB
DEFAULT_THEME_G = 0    # Default theme color RGB
DEFAULT_THEME_B = 200  # Default theme color RGB


class BreakoutGraphics:
    """
    The class of whole breakout game graphics.
    """

    def __init__(self, title='Breakout', num_lives=NUM_LIVES):

        # Create a graphical window, with some extra space
        self.__window_width = BRICK_COLS * (BRICK_WIDTH + BRICK_SPACING) - BRICK_SPACING
        self.__window_height = BRICK_OFFSET + 3 * (BRICK_ROWS * (BRICK_HEIGHT + BRICK_SPACING) - BRICK_SPACING)
        self.__window = GWindow(width=self.__window_width, height=self.__window_height, title=title)

        # global(across pages) elements
        self.__page_no = 1
        self.__title_label = GLabel("BreakOut Game")
        self.__paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.__paddle.filled = True
        self.__ball = None
        self.__ball_height = 0
        self.__ball_width = 0
        self.create_ball()
        self.__theme_r = DEFAULT_THEME_R
        self.__theme_g = DEFAULT_THEME_G
        self.__theme_b = DEFAULT_THEME_B
        self.__random_map_on = False
        self.__color_defense_on = True
        self.__effect_ball_on = True
        self.__background_ball_x = 0
        self.__background_ball_y = 0
        self.__name_label = GLabel("SC101_Assignment2_Di Cheng")
        self.__name_label.font = "Verdana-12"
        self.__name_label.color = (0, 0, 150)
        self.__return_menu_label = GItem("Return Menu", font_size=15)
        self.__new_record = False
        self.__your_score = 0
        self.__life_point = 0
        self.__top_1 = 0
        self.__top_2 = 0
        self.__top_3 = 0
        self.__top_4 = 0
        self.__top_5 = 0

        # page_1 elements
        self.__start_game_label = GItem("Start", font_size=15)
        self.__game_setting_label = GItem("Setting", font_size=15)
        self.__score_board_label = GItem("ScoreBoard", font_size=15)
        self.__exit_label = GItem("Exit", font_size=15)

        # page_2 elements
        # paddle
        self.__paddle_center_x = 0
        # bricks
        self.__brick_nums = 0
        # extra ball
        self.__have_extra_ball = False
        self.__extra_ball = None
        self.__ball_count = 0
        # effect ball
        self.__effect_ball_show = False
        self.__effecting = False
        self.__power_ball = False
        self.__effecting_type = 0
        self.__effecting_no = 0
        self.__effecting_time = 0
        self.__effecting_count = 0
        self.__effect_ball = None
        # game flags
        self.__game_on = False
        self.__game_over = False
        self.__clear_game = False
        self.__game_pause = False
        # label
        self.__score_label = None
        self.__count_down_bar = None
        self.__effect_ball_desc = None
        self.__life_point_text = ""
        self.__life_point_default = num_lives
        self.__life_point_label = None
        self.__game_end_label = GItem("", font_size=17)
        self.__bonus_add_label = GItem("", font_size=15)
        self.__hint_label = GItem("Click to Start", font_size=15)
        self.__pause_label = GItem("PAUSE", font_size=15)
        self.__pause_label.color = (200, 200, 200)
        self.__pause_label_text = GItem("PAUSE", font_size=17)
        self.__quit_label = GItem("QUIT", font_size=15)
        self.__quit_label.color = (200, 200, 200)

        # page_3 elements
        self.__choose_theme_label = GItem("Choose Theme Color : ", font_size=15)
        self.__random_map_label = GItem("Random Map : " + self.get_boolean_icon(self.__random_map_on), font_size=15)
        self.__color_defense_label = GItem("Color Defense : " + self.get_boolean_icon(self.__color_defense_on), font_size=15)
        self.__effect_ball_label = GItem("Effect Ball : " + self.get_boolean_icon(self.__effect_ball_on), font_size=15)
        self.__clean_scoreboard_label = GItem("Clean ScoreBoard", font_size=15)
        self.__theme_item_r = GOvalItem(BALL_RADIUS * 2, BALL_RADIUS * 2, r=200, g=0, b=0)
        self.__theme_item_rg = GOvalItem(BALL_RADIUS * 2, BALL_RADIUS * 2, r=200, g=200, b=0)
        self.__theme_item_g = GOvalItem(BALL_RADIUS * 2, BALL_RADIUS * 2, r=0, g=200, b=0)
        self.__theme_item_gb = GOvalItem(BALL_RADIUS * 2, BALL_RADIUS * 2, r=0, g=200, b=200)
        self.__theme_item_b = GOvalItem(BALL_RADIUS * 2, BALL_RADIUS * 2, r=0, g=0, b=200)
        self.__theme_item_rb = GOvalItem(BALL_RADIUS * 2, BALL_RADIUS * 2, r=200, g=0, b=200)

        # page_4 elements
        self.__your_score_label = None
        self.__top_1_label = None
        self.__top_2_label = None
        self.__top_3_label = None
        self.__top_4_label = None
        self.__top_5_label = None

        # Initialize mouse listeners
        onmouseclicked(self.click_event)
        onmousemoved(self.move_event)

        # Execute default first page
        self.page_1()

    def page_1(self):
        """
        Default first page of BreakOut Game, contains game menu of start game, game setting, scoreboard and exit itmes.
        """
        # Add title
        self.__title_label.text = "BreakOut Game"
        self.__title_label.font = "Verdana-40-bold-italic"
        self.__title_label.color = self.__ball.color
        self.__window.add(self.__title_label, self.__window.width / 2 - self.__title_label.width / 2, self.__window_height / 2 - self.__title_label.height * 3)
        # Add menu
        self.__window.add(self.__start_game_label, self.__window.width / 2 - self.__title_label.width / 5, self.__window_height / 2 + self.__start_game_label.height * 3)
        self.__window.add(self.__game_setting_label, self.__window.width / 2 - self.__title_label.width / 5, self.__start_game_label.y + self.__game_setting_label.height * 2)
        self.__window.add(self.__score_board_label, self.__window.width / 2 - self.__title_label.width / 5, self.__game_setting_label.y + self.__score_board_label.height * 2)
        self.__window.add(self.__exit_label, self.__window.width / 2 - self.__title_label.width / 5, self.__score_board_label.y + self.__exit_label.height*3)
        # Setting background
        self.set_background()
        # Add name label
        self.__window.add(self.__name_label, self.__window.width - self.__name_label.width, self.__window.height)

    def page_2(self):
        """
        The main breakout game page, contains all the elements in needs.
        Including bricks, paddle, ball, extra ball, effect ball and labels.
        """
        # Add a paddle
        self.__paddle.color = (0, 0, 0)
        self.__paddle.fill_color = (0, 0, 0)
        self.__window.add(self.__paddle, self.__window.width / 2 - self.__paddle.width / 2, self.__window.height - PADDLE_OFFSET)
        self.__paddle_center_x = self.__paddle.x + self.__paddle.width/2
        # Add a filled ball on the center of paddle in the graphical window
        self.create_ball()
        self.__window.add(self.__ball, self.__paddle_center_x - self.__ball_width / 2, self.__paddle.y - self.__ball_height)
        # Prepare extra filled ball setting
        self.__have_extra_ball = False
        self.__extra_ball = None
        self.__ball_count = 1
        self.__effect_ball_show = False
        self.__effecting = False
        self.__effecting_type = 0
        self.__effecting_no = 0
        self.__effecting_time = 0
        self.__effecting_count = 0
        self.__effect_ball = None
        self.__game_on = False
        self.__game_over = False
        self.__clear_game = False
        self.__game_pause = False
        # Add labels
        self.__score_label = GItem("Your Score : " + str(self.__your_score), font_size=15)
        self.__window.add(self.__score_label, 0, self.__score_label.height)
        self.__count_down_bar = GLabel("")
        self.__count_down_bar.font = "-17"
        self.__window.add(self.__count_down_bar, 0, self.__window.height)
        self.__effect_ball_desc = GItem("", font_size=15)
        self.__window.add(self.__effect_ball_desc, 0, self.__window.height)
        self.__life_point = self.__life_point_default
        self.__life_point_text = ""
        for i in range(self.__life_point):
            self.__life_point_text += "❤"
        self.__life_point_label = GLabel(self.__life_point_text)
        self.__life_point_label.font = "-22"
        self.__life_point_label.color = (150, 0, 0)
        self.__window.add(self.__life_point_label, self.__window.width - self.__life_point_label.width, self.__window.height)
        self.__window.add(self.__game_end_label, 0, 0)
        self.__window.add(self.__bonus_add_label, 0, 0)
        self.__window.add(self.__hint_label, self.__window.width / 2 - self.__hint_label.width / 2, self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height + self.__hint_label.height * 2)
        self.__window.add(self.__pause_label, self.__window.width - self.__pause_label.width, self.__paddle.y - self.__paddle.height * 2)
        self.__window.add(self.__pause_label_text, self.__window.width / 2 - self.__pause_label_text.width / 2, 0)
        self.__pause_label_text.color = (self.__theme_r, self.__theme_g, self.__theme_b)
        self.__window.add(self.__quit_label, self.__window.width - self.__quit_label.width, self.__quit_label.height)
        # Setting bricks
        self.__brick_nums = 0
        self.set_bricks()

    def page_3(self):
        """
        Game Setting Page, where user can setup the theme color,
        switch game mode of random map, color defensed and effect balls, reset scoreboard as well.
        """
        # Add title
        self.__title_label.text = "GameSetting"
        self.__title_label.font = "Verdana-40-bold-italic"
        self.__title_label.color = self.__ball.color
        self.__window.add(self.__title_label, self.__window.width / 2 - self.__title_label.width / 2, self.__window_height / 2 - self.__title_label.height * 3)
        # Add setting item
        self.__window.add(self.__choose_theme_label, self.__window.width / 2 - self.__title_label.width / 4,  self.__window_height / 2)
        # Add theme color select item
        self.__window.add(self.__theme_item_r, self.__window.width / 2 - self.__title_label.width / 4, self.__window_height / 2 + self.__choose_theme_label.height)
        self.__window.add(self.__theme_item_r.get_item(), self.__theme_item_r.get_item_x(), self.__theme_item_r.get_item_y())
        self.__window.add(self.__theme_item_rg, self.__theme_item_r.x + self.__theme_item_r.width + self.__theme_item_r.width/2, self.__window_height / 2 + self.__choose_theme_label.height)
        self.__window.add(self.__theme_item_rg.get_item(), self.__theme_item_rg.get_item_x(), self.__theme_item_rg.get_item_y())
        self.__window.add(self.__theme_item_g, self.__theme_item_rg.x + self.__theme_item_rg.width + self.__theme_item_rg.width/2, self.__window_height / 2 + self.__choose_theme_label.height)
        self.__window.add(self.__theme_item_g.get_item(), self.__theme_item_g.get_item_x(), self.__theme_item_g.get_item_y())
        self.__window.add(self.__theme_item_gb, self.__theme_item_g.x + self.__theme_item_g.width + self.__theme_item_g.width/2, self.__window_height / 2 + self.__choose_theme_label.height)
        self.__window.add(self.__theme_item_gb.get_item(), self.__theme_item_gb.get_item_x(), self.__theme_item_gb.get_item_y())
        self.__window.add(self.__theme_item_b, self.__theme_item_gb.x + self.__theme_item_gb.width + self.__theme_item_gb.width/2, self.__window_height / 2 + self.__choose_theme_label.height)
        self.__window.add(self.__theme_item_b.get_item(), self.__theme_item_b.get_item_x(), self.__theme_item_b.get_item_y())
        self.__window.add(self.__theme_item_rb, self.__theme_item_b.x + self.__theme_item_b.width + self.__theme_item_b.width/2, self.__window_height / 2 + self.__choose_theme_label.height)
        self.__window.add(self.__theme_item_rb.get_item(), self.__theme_item_rb.get_item_x(), self.__theme_item_rb.get_item_y())
        # Add setting labels
        self.__window.add(self.__random_map_label, self.__window.width / 2 - self.__title_label.width / 4, self.__theme_item_r.y + self.__theme_item_r.height + self.__random_map_label.height * 2)
        self.__window.add(self.__color_defense_label, self.__window.width / 2 - self.__title_label.width / 4, self.__random_map_label.y + self.__color_defense_label.height * 2)
        self.__window.add(self.__effect_ball_label, self.__window.width / 2 - self.__title_label.width / 4, self.__color_defense_label.y + self.__effect_ball_label.height * 2)
        self.__window.add(self.__clean_scoreboard_label, self.__window.width / 2 - self.__title_label.width / 4, self.__effect_ball_label.y + self.__clean_scoreboard_label.height * 2)
        # Add return menu label
        self.__window.add(self.__return_menu_label, self.__window.width / 2 - self.__title_label.width / 4, self.__clean_scoreboard_label.y + self.__return_menu_label.height * 3)
        # Setting background
        self.set_background()
        # Add name Label
        self.__name_label.text = "SC101_Assignment2_Di Cheng"
        self.__name_label.font = "Verdana-12"
        self.__name_label.color = (0, 0, 150)
        self.__window.add(self.__name_label, self.__window.width - self.__name_label.width, self.__window.height)

    def page_4(self):
        """
        ScoreBoard Page, Displaying top 5 scores record while program is running.
        """
        self.update_scoreboard()
        # Add title
        self.__title_label.text = "ScoreBoard"
        self.__title_label.font = "Verdana-40-bold-italic"
        self.__title_label.color = self.__ball.color
        self.__window.add(self.__title_label, self.__window.width / 2 - self.__title_label.width / 2, self.__window_height / 2 - self.__title_label.height * 3)
        # Add scoreboard top 5
        self.__your_score_label = GItem("Your score :  " + str(self.__your_score), font_size=15)
        self.__your_score_label.font = "Verdana-15-bold-italic"
        self.__your_score_label.color = (150, 0, 0)
        if self.__your_score != 0:
            if self.__new_record:
                self.__your_score_label.text = "New Record!! Your score :  " + str(self.__your_score)
            self.__window.add(self.__your_score_label, self.__window.width / 2 - self.__your_score_label.width /2, self.__window_height / 2 - self.__your_score_label.height * 3)
            self.__your_score = 0
            self.__new_record = False
        self.__top_1_label = GItem("Top 1 :  " + str(self.__top_1), font_size=15)
        self.__top_2_label = GItem("Top 2 :  " + str(self.__top_2), font_size=15)
        self.__top_3_label = GItem("Top 3 :  " + str(self.__top_3), font_size=15)
        self.__top_4_label = GItem("Top 4 :  " + str(self.__top_4), font_size=15)
        self.__top_5_label = GItem("Top 5 :  " + str(self.__top_5), font_size=15)
        self.__window.add(self.__top_1_label, self.__window.width / 2 - self.__title_label.width / 6, self.__window_height / 2 + self.__top_1_label.height)
        self.__window.add(self.__top_2_label, self.__window.width / 2 - self.__title_label.width / 6, self.__top_1_label.y + self.__top_2_label.height * 2)
        self.__window.add(self.__top_3_label, self.__window.width / 2 - self.__title_label.width / 6, self.__top_2_label.y + self.__top_3_label.height * 2)
        self.__window.add(self.__top_4_label, self.__window.width / 2 - self.__title_label.width / 6, self.__top_3_label.y + self.__top_4_label.height * 2)
        self.__window.add(self.__top_5_label, self.__window.width / 2 - self.__title_label.width / 6, self.__top_4_label.y + self.__top_5_label.height * 2)
        # Add return menu label
        self.__window.add(self.__return_menu_label, self.__window.width / 2 - self.__title_label.width / 6, self.__top_5_label.y + self.__return_menu_label.height * 3)
        # Setting background
        self.set_background()
        # Add name Label
        __today = date.today()
        __today_str = __today.strftime("%Y-%b-%d")
        self.__name_label.text = __today_str
        self.__name_label.font = "Verdana-12"
        self.__name_label.color = (0, 0, 150)
        self.__window.add(self.__name_label, self.__window.width - self.__name_label.width, self.__window.height)

    def set_background(self):
        """
        This background is a simulated breakout game balls bouncing for page 1 , 3, 4.
        """
        if self.__ball.get_dx() == 0:
            self.__window.add(self.__paddle, self.__window.width / 2 - self.__paddle.width / 2, self.__window.height - PADDLE_OFFSET)
            self.__paddle_center_x = self.__paddle.x + self.__paddle.width / 2
            self.__window.add(self.__ball, self.__paddle_center_x - self.__ball_width / 2, self.__paddle.y - self.__ball_height)
            self.__ball.initial_velocity()
        else:
            self.__window.add(self.__ball, self.__ball.get_background_x(), self.__ball.get_background_y())
            self.__window.add(self.__paddle, self.__ball.x - self.__paddle.width / 2 + self.__ball_width / 2, self.__window.height - PADDLE_OFFSET)

    def background_ball_hit_something(self):
        """
        For background ball bouncing.
        """
        for x in range(2):
            for y in range(2):
                maybe_hit_obj = self.__window.get_object_at(self.__ball.x + x * 2 * BALL_RADIUS, self.__ball.y + y * 2 * BALL_RADIUS)
                if maybe_hit_obj is not None and maybe_hit_obj is self.__paddle:
                    return True

    def set_bricks(self):
        """
        When page 2 (main game page) shows up,
        setting the bricks depends on the setting of random map switch.
        """
        __col_brick_num = BRICK_ROWS
        __brick_lvl_lst = DEFAULT_BRICK_LVL_LST
        if self.__random_map_on:
            __row_num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            for i in range(len(__brick_lvl_lst)):
                __tmp_lst = []
                for j in range(3):
                    __tmp_lst.append(__row_num_lst.pop(random.randint(1, len(__row_num_lst)) - 1))
                __brick_lvl_lst[i] = __tmp_lst
            if len(__row_num_lst) > 0:
                for i in range(len(__row_num_lst)):
                    __brick_lvl_lst[1].append(__row_num_lst[i])
        for x in range(BRICK_ROWS):
            if self.__random_map_on:
                __col_brick_num = random.randint(3, 10)
            for y in range(BRICK_COLS):
                # (This line switch for building only one row of bricks.)
                # if y == 9:
                if y < __col_brick_num:
                    __brick = GBrick(BRICK_WIDTH, BRICK_HEIGHT, row=y+1, brick_lvl_lst=__brick_lvl_lst, theme_r=self.__theme_r, theme_g=self.__theme_g, theme_b=self.__theme_b, color_defense_on=self.__color_defense_on)
                    self.__window.add(__brick, x * (BRICK_WIDTH + BRICK_SPACING), BRICK_OFFSET + y * (BRICK_HEIGHT + BRICK_SPACING))
                    self.__brick_nums += 1

    def ball_hit_something(self):
        """
        For main ball on screen detecting is hitting something or not.
        """
        for x in range(2):
            for y in range(2):
                maybe_hit_obj = self.__window.get_object_at(self.__ball.x + x * 2 * BALL_RADIUS, self.__ball.y + y * 2 * BALL_RADIUS)
                if maybe_hit_obj is None or maybe_hit_obj is self.__effect_ball or (self.__effect_ball is not None and maybe_hit_obj is self.__effect_ball.get_effect_label()) or maybe_hit_obj is self.__score_label or maybe_hit_obj is self.__game_end_label or maybe_hit_obj is self.__pause_label_text or maybe_hit_obj is self.__your_score_label or maybe_hit_obj is self.__bonus_add_label or maybe_hit_obj is self.__hint_label or maybe_hit_obj is self.__effect_ball_desc or maybe_hit_obj is self.__count_down_bar or maybe_hit_obj is self.__pause_label or maybe_hit_obj is self.__quit_label or maybe_hit_obj is self.__extra_ball or maybe_hit_obj is self.__life_point_label:
                    pass
                else:
                    # when hit bricks
                    if maybe_hit_obj.y < self.__paddle.y:
                        if self.__effect_ball_on and not self.__effecting and not self.__effect_ball_show and maybe_hit_obj.have_effect_ball():
                            self.create_effect_ball(maybe_hit_obj.x + maybe_hit_obj.width/2, maybe_hit_obj.y + maybe_hit_obj.height/2)
                        self.__your_score += maybe_hit_obj.get_point(self.__power_ball)
                        maybe_hit_obj.set_brick_life(-1, self.__power_ball)
                        self.update_scores()
                        if maybe_hit_obj.remove_brick():
                            self.__window.remove(maybe_hit_obj)
                            self.__brick_nums -= 1
                        self.check_bricks_nums()
                        if self.__power_ball:
                            return False
                    # when hit paddle, prevent loop in +-dy
                    if maybe_hit_obj.y >= self.__paddle.y and self.__ball.get_dy() < 0:
                        return False
                    return True

    def extra_ball_hit_something(self):
        """
        For extra ball on screen detecting is hitting something or not.
        """
        for x in range(2):
            for y in range(2):
                maybe_hit_obj = self.__window.get_object_at(self.__extra_ball.x + x * 2 * BALL_RADIUS, self.__extra_ball.y + y * 2 * BALL_RADIUS)
                if maybe_hit_obj is None or maybe_hit_obj is self.__effect_ball or (self.__effect_ball is not None and maybe_hit_obj is self.__effect_ball.get_effect_label()) or maybe_hit_obj is self.__score_label or maybe_hit_obj is self.__game_end_label or maybe_hit_obj is self.__pause_label_text or maybe_hit_obj is self.__your_score_label or maybe_hit_obj is self.__bonus_add_label or maybe_hit_obj is self.__hint_label or maybe_hit_obj is self.__effect_ball_desc or maybe_hit_obj is self.__count_down_bar or maybe_hit_obj is self.__ball or maybe_hit_obj is self.__pause_label or maybe_hit_obj is self.__quit_label or maybe_hit_obj is self.__life_point_label:
                    pass
                else:
                    # when hit bricks
                    if maybe_hit_obj.y < self.__paddle.y:
                        if self.__effect_ball_on and not self.__effecting and not self.__effect_ball_show and maybe_hit_obj.have_effect_ball():
                            self.create_effect_ball(maybe_hit_obj.x + maybe_hit_obj.width / 2, maybe_hit_obj.y + maybe_hit_obj.height / 2)
                        self.__your_score += maybe_hit_obj.get_point(self.__power_ball)
                        maybe_hit_obj.set_brick_life(-1, self.__power_ball)
                        self.update_scores()
                        if maybe_hit_obj.remove_brick():
                            self.__window.remove(maybe_hit_obj)
                            self.__brick_nums -= 1
                        self.check_bricks_nums()
                        if self.__power_ball:
                            return False
                    # when hit paddle, prevent loop in +-dy
                    if maybe_hit_obj.y >= self.__paddle.y and self.__extra_ball.get_dy() < 0:
                        return False
                    return True

    def check_bricks_nums(self):
        """
        Check the remain brick number is down to zero each time when ball hit something, to decide if it's game clear.
        """
        if self.__brick_nums == 0:
            if self.__ball is not None:
                self.__ball.set_speed(1.5)
            if self.__have_extra_ball:
                self.__extra_ball.set_speed(1.5)
            self.__game_end_label.text = "GAME CLEAR"
            self.__game_end_label.color = (0, 0, 150)
            self.__game_end_label.x = self.__window.width / 2 - self.__game_end_label.width / 2
            self.__game_end_label.y = self.__window.height / 2 + self.__ball_height / 2 - self.__game_end_label.height
            self.__bonus_add_label.text = self.__life_point_text + " = Bonus +" + str(self.__life_point * 50)
            self.__your_score += self.__life_point * 50
            self.__your_score_label = GItem("Your score :  " + str(self.__your_score), font_size=15)
            if self.__your_score > self.__top_1:
                self.__your_score_label.text = "New Record!! Your score :  " + str(self.__your_score)
                self.__window.add(self.__your_score_label, self.__window.width / 2 - self.__your_score_label.width /2, self.__window_height / 2 - self.__your_score_label.height * 3)
            self.__bonus_add_label.x = self.__window.width / 2 - self.__bonus_add_label.width / 2
            self.__bonus_add_label.y = self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height + self.__bonus_add_label.height * 2
            self.__hint_label.text = "Click to Next Game"
            self.__hint_label.x = self.__window.width / 2 - self.__hint_label.width / 2
            self.__hint_label.y = self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height + self.__hint_label.height * 4
            self.__clear_game = True
            self.set_effect_default()

    def update_scores(self):
        """
        Update score label to show current score.
        """
        self.__score_label.text = "Your Score : " + str(self.__your_score)

    def create_effect_ball(self, x, y):
        """
        Create a effect ball on the given x, y (where was the brick been hit).
        """
        self.__effect_ball = GEffectBall(EFFECT_BALL_SIZE, EFFECT_BALL_SIZE, have_extra_ball=self.__have_extra_ball)
        self.__effecting_time = self.__effect_ball.get_effect_time()
        self.__window.add(self.__effect_ball, x, y)
        self.__window.add(self.__effect_ball.get_effect_label(), self.__effect_ball.get_effect_label_x(), self.__effect_ball.get_effect_label_y())
        self.__effect_ball_show = True
        self.create_effect_ball_meta()

    def create_effect_ball_meta(self):
        """
        The meta info for current effect ball.
        """
        if self.__effect_ball_show:
            self.__count_down_bar.color = self.__effect_ball.color
            self.__effect_ball_desc.color = self.__effect_ball.color
            self.__effect_ball_desc.text = self.__effect_ball.get_effect_desc()

    def check_effect_ball_hit_paddle(self):
        """
        For effect ball on screen detecting is hitting paddle or not. If hit paddle, means user get the effect.
        """
        if self.__effect_ball is not None:
            # this flag control make sure paddle only get effect ball once.
            __already_get_ball = False
            for x in range(2):
                for y in range(2):
                    maybe_hit_obj = self.__window.get_object_at(self.__effect_ball.x + x * EFFECT_BALL_SIZE, self.__effect_ball.y + y * EFFECT_BALL_SIZE)
                    if maybe_hit_obj is None or maybe_hit_obj is self.__ball or maybe_hit_obj is self.__extra_ball or maybe_hit_obj is self.__pause_label_text:
                        pass
                    else:
                        if maybe_hit_obj is self.__paddle and not __already_get_ball:
                            __already_get_ball = True
                            self.do_effect()
                            self.check_effect_time()
                            self.__window.remove(self.__effect_ball.get_effect_label())
                            self.__window.remove(self.__effect_ball)
                            self.__effect_ball_show = False
                            self.__effect_ball_desc.text = ""

    def do_effect(self):
        """
        Get the effect accordingly.
        """
        if not self.__effecting:
            self.__effecting_type = self.__effect_ball.get_effect_type()
            self.__effecting_no = self.__effect_ball.get_effect_no()
            if self.__effecting_type != 4:
                self.__effecting_time = self.__effect_ball.get_effect_time()
                self.__effecting = True
        if self.__effecting_type == 1:
            self.paddle_effect()
        elif self.__effecting_type == 2:
            self.ball_effect()
        elif self.__effecting_type == 3:
            self.power_effect()
        elif self.__effecting_type == 4:
            self.gain_effect()

    def clean_effect(self):
        """
        Reset the effect to default.
        """
        if self.__effecting_type == 1:
            self.paddle_effect()
        elif self.__effecting_type == 2:
            self.ball_effect()
        elif self.__effecting_type == 3:
            self.power_effect()

    def paddle_effect(self):
        """
        The paddle effect.
        """
        if self.__effecting_no == 1:
            self.__window.remove(self.__paddle)
            self.__paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
            self.__paddle.filled = True
            self.__window.add(self.__paddle, self.__paddle_center_x - self.__paddle.width/2, self.__window.height - PADDLE_OFFSET)
            self.__effecting = False
        elif self.__effecting_no == 2:
            self.__window.remove(self.__paddle)
            self.__paddle = GRect(PADDLE_WIDTH * 2, PADDLE_HEIGHT)
            self.__paddle.filled = True
            self.__window.add(self.__paddle, self.__paddle_center_x - self.__paddle.width/2, self.__window.height - PADDLE_OFFSET)
        elif self.__effecting_no == 3:
            self.__window.remove(self.__paddle)
            self.__paddle = GRect(PADDLE_WIDTH / 2, PADDLE_HEIGHT)
            self.__paddle.filled = True
            self.__window.add(self.__paddle, self.__paddle_center_x - PADDLE_WIDTH/2, self.__window.height - PADDLE_OFFSET)

    def ball_effect(self):
        """
        The ball effect.
        """
        if self.__effecting_no == 1:
            if self.__ball is not None:
                self.get_ball().set_speed(1)
            if self.__have_extra_ball:
                self.get_extra_ball().set_speed(1)
            self.__effecting = False
        elif self.__effecting_no == 2:
            if self.__ball is not None:
                self.get_ball().set_speed(1.25)
            if self.__have_extra_ball:
                self.get_extra_ball().set_speed(1.25)
        elif self.__effecting_no == 3:
            if self.__ball is not None:
                self.get_ball().set_speed(0.5)
            if self.__have_extra_ball:
                self.get_extra_ball().set_speed(0.5)

    def power_effect(self):
        """
        The power ball effect.
        """
        if self.__effecting_no == 1:
            self.__power_ball = False
            self.__effecting = False
        elif self.__effecting_no == 2:
            self.__power_ball = True

    def gain_effect(self):
        """
        Gain another life point or extra ball effect.
        """

        if self.__effecting_no == 1:
            self.__life_point += 1
            self.update_life_point()
        elif self.__effecting_no == 2:
            self.__ball_count += 1
            self.create_extra_ball()

    def create_ball(self):
        if self.__ball is None:
            self.__ball = GBall(BALL_RADIUS * 2, BALL_RADIUS * 2)
            self.__ball.filled = True
            self.__ball.color = (0, 0, 0)
            self.__ball.fill_color = (0, 0, 0)
            self.__ball_height = self.__ball.height
            self.__ball_width = self.__ball.width
        else:
            self.__ball.filled = True
            self.__ball.color = (0, 0, 0)
            self.__ball.fill_color = (0, 0, 0)

    def remove_ball(self):
        """
        Remove the ball.
        """
        if self.__ball.y > self.__window.height:
            self.__window.remove(self.__ball)
            self.__ball = None

    def create_extra_ball(self):
        """
        To create an extra ball.
        """
        if not self.__have_extra_ball:
            self.__extra_ball = GBall(BALL_RADIUS * 2, BALL_RADIUS * 2)
            self.__have_extra_ball = True
            self.__extra_ball.filled = True
            self.__extra_ball.color = (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))
            self.__extra_ball.fill_color = self.__extra_ball.color
            self.__window.add(self.__extra_ball, self.__paddle_center_x - self.__extra_ball.width / 2, self.__paddle.y - self.__extra_ball.height)

    def remove_extra_ball(self):
        """
        Remove an extra ball.
        """
        if self.__have_extra_ball:
            self.__have_extra_ball = False
            self.__window.remove(self.__extra_ball)
            self.__extra_ball = None

    def check_effect_time(self):
        """
        Check the effect time per query(1000/12 millisecond), and log per seconds.
        """
        if not self.__game_pause:
            if self.__effecting:
                if self.__effecting_count == 0:
                    __count_down_bar = ""
                    for i in range(self.__effecting_time):
                        __count_down_bar += "▃"
                    self.__count_down_bar.text = __count_down_bar
                self.__effecting_count += 1
                if self.__effecting_count > 121:  #  1000/120
                    self.__effecting_time -= 1  # 1 sec passed
                    __count_down_bar = ""
                    for i in range(self.__effecting_time):
                        __count_down_bar += "▃"
                    self.__count_down_bar.text = __count_down_bar
                    self.__effecting_count = 0
                    if self.__effecting_time == 0:
                        self.__effecting_no = 1
                        self.do_effect()

    def click_event(self, mouse_obj):
        """
        Setting events when mouse clicked on different pages/conditions.
        """
        # page 1: menu page
        if self.__page_no == 1:
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is not None:
                if maybe_obj is self.__start_game_label:
                    self.__window.clear()
                    self.__page_no = 2
                    self.__life_point = 0  # every new start reset the life point
                    self.__effecting_no = 1
                    self.clean_effect()
                    self.page_2()
                if maybe_obj is self.__game_setting_label:
                    self.__ball.set_background_xy(self.__ball.x, self.__ball.y)
                    self.__window.clear()
                    self.__page_no = 3
                    self.page_3()
                if maybe_obj is self.__score_board_label:
                    self.__ball.set_background_xy(self.__ball.x, self.__ball.y)
                    self.__window.clear()
                    self.__page_no = 4
                    self.page_4()
                if maybe_obj is self.__exit_label:
                    self.__window.close()
        # page 2: game page
        elif self.__page_no == 2:
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is self.__quit_label:
                if self.__your_score != 0:
                    self.__window.clear()
                    self.set_ball_position()
                    self.__page_no = 4
                    self.page_4()
                else:
                    self.__window.clear()
                    self.set_ball_position()
                    self.__page_no = 1
                    self.page_1()
            if not self.__game_pause:
                if mouse_obj is not None and maybe_obj is self.__pause_label:
                    self.__pause_label_text.y = self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height
                    self.__hint_label.text = "Click to Continue"
                    self.__hint_label.x = self.__window.width / 2 - self.__hint_label.width / 2
                    self.__hint_label.y = self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height + self.__hint_label.height * 4
                    self.game_pause()
                if not self.__game_on and not self.__game_pause:
                    self.__ball.initial_velocity()
                    self.__hint_label.y = 0
                    self.__game_on = True
                elif self.__have_extra_ball and self.__extra_ball.get_dy() == 0 and not self.__game_pause:
                    if self.__ball is not None:
                        self.__extra_ball.follow_velocity(self.__ball.get_dx())
                    else:
                        self.__extra_ball.initial_velocity()
                elif self.__game_over:
                    self.__window.clear()
                    self.__page_no = 4
                    self.page_4()
                elif self.__clear_game:
                    if maybe_obj is not self.__quit_label:
                        self.__window.clear()
                        self.__ball = None
                        self.remove_extra_ball()
                        # self.set_ball_position()
                        self.clean_effect()
                        self.__clear_game = False
                        self.__random_map_on = True
                        self.__page_no = 2
                        self.page_2()
                    else:
                        self.__window.clear()
                        self.set_ball_position()
                        self.__clear_game = False
                        self.__page_no = 4
                        self.page_4()
            else:
                self.game_resume()
                self.__pause_label_text.y = 0
                self.__hint_label.y = 0
        # page 3: setting page
        elif self.__page_no == 3:
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is not None:
                # theme color
                if maybe_obj is self.__theme_item_r.get_item():
                    self.set_theme_color(self.__theme_item_r.get_item_r(), self.__theme_item_r.get_item_g(), self.__theme_item_r.get_item_b())
                elif maybe_obj is self.__theme_item_rg.get_item():
                    self.set_theme_color(self.__theme_item_rg.get_item_r(), self.__theme_item_rg.get_item_g(), self.__theme_item_rg.get_item_b())
                elif maybe_obj is self.__theme_item_g.get_item():
                    self.set_theme_color(self.__theme_item_g.get_item_r(), self.__theme_item_g.get_item_g(), self.__theme_item_g.get_item_b())
                elif maybe_obj is self.__theme_item_gb.get_item():
                    self.set_theme_color(self.__theme_item_gb.get_item_r(), self.__theme_item_gb.get_item_g(), self.__theme_item_gb.get_item_b())
                elif maybe_obj is self.__theme_item_b.get_item():
                    self.set_theme_color(self.__theme_item_b.get_item_r(), self.__theme_item_b.get_item_g(), self.__theme_item_b.get_item_b())
                elif maybe_obj is self.__theme_item_rb.get_item():
                    self.set_theme_color(self.__theme_item_rb.get_item_r(), self.__theme_item_rb.get_item_g(), self.__theme_item_rb.get_item_b())
                elif maybe_obj is self.__random_map_label:
                    self.__random_map_on = self.switch_boolean(self.__random_map_on)
                    self.__random_map_label.set_label_text("Random Map : " + self.get_boolean_icon(self.__random_map_on))
                elif maybe_obj is self.__choose_theme_label:
                    pass
                elif maybe_obj is self.__color_defense_label:
                    self.__color_defense_on = self.switch_boolean(self.__color_defense_on)
                    self.__color_defense_label.set_label_text("Color Defense : " + self.get_boolean_icon(self.__color_defense_on))
                elif maybe_obj is self.__effect_ball_label:
                    self.__effect_ball_on = self.switch_boolean(self.__effect_ball_on)
                    self.__effect_ball_label.set_label_text("Effect Ball : " + self.get_boolean_icon(self.__effect_ball_on))
                elif maybe_obj is self.__clean_scoreboard_label:
                    self.clean_scoreboard()
                    self.__ball.set_background_xy(self.__ball.x, self.__ball.y)
                    self.__window.clear()
                    self.__page_no = 4
                    self.page_4()
                elif maybe_obj is self.__return_menu_label:
                    self.__ball.set_background_xy(self.__ball.x, self.__ball.y)
                    self.__window.clear()
                    self.__page_no = 1
                    self.page_1()
        # page 4: scoreboard
        elif self.__page_no == 4:
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is not None and maybe_obj is self.__return_menu_label:
                self.__ball.set_background_xy(self.__ball.x, self.__ball.y)
                self.__window.clear()
                self.__page_no = 1
                self.page_1()

    def move_event(self, mouse_obj):
        """
        Setting events when mouse moved on different pages/conditions.
        """
        # page 1: menu page
        if self.__page_no == 1:
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is None:
                if self.__start_game_label.color != self.__title_label.color:
                    self.__start_game_label.hover_out()
                if self.__game_setting_label.color != self.__title_label.color:
                    self.__game_setting_label.hover_out()
                if self.__score_board_label.color != self.__title_label.color:
                    self.__score_board_label.hover_out()
                if self.__exit_label.color != self.__title_label.color:
                    self.__exit_label.hover_out()
            elif maybe_obj is self.__start_game_label or maybe_obj is self.__game_setting_label or maybe_obj is self.__score_board_label or maybe_obj is self.__exit_label:
                maybe_obj.hover_on()
        # page 2: game page
        elif self.__page_no == 2:
            # pause & quit
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is None:
                if self.__quit_label.color != self.__score_label.color:
                    self.__quit_label.hover_out_no_hand()
                if self.__pause_label.color != self.__score_label.color:
                    self.__pause_label.hover_out_no_hand()
                if self.__game_pause:
                    self.__pause_label_text.y = self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height
                elif self.__pause_label_text.y != 0:
                    self.__pause_label_text.y = 0
            elif maybe_obj is self.__quit_label:
                self.__quit_label.hover_on_no_hand()
            elif maybe_obj is self.__pause_label:
                self.__pause_label.hover_on_no_hand()
            if not self.__game_pause:
                # ball & paddle
                if mouse_obj.x - self.__paddle.width / 2 <= 0:
                    self.__paddle.x = 0
                elif mouse_obj.x + self.__paddle.width / 2 >= self.__window_width:
                    self.__paddle.x = self.__window_width - self.__paddle.width
                else:
                    self.__paddle.x = mouse_obj.x - self.__paddle.width / 2
                self.__paddle_center_x = self.__paddle.x + self.__paddle.width / 2
                if not self.__game_on:
                    self.__ball.x = self.__paddle_center_x - self.__ball_width / 2
                elif self.__have_extra_ball and self.__extra_ball.get_dy() == 0:
                    self.__extra_ball.x = self.__paddle_center_x - self.__extra_ball.width / 2
        # page 3: setting page
        elif self.__page_no == 3:
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is None:
                if self.__choose_theme_label.color != self.__title_label.color:
                    self.__choose_theme_label.hover_out()
                if self.__theme_item_r.color != self.__title_label.color:
                    self.__theme_item_r.hover_out()
                if self.__theme_item_rg.color != self.__title_label.color:
                    self.__theme_item_rg.hover_out()
                if self.__theme_item_g.color != self.__title_label.color:
                    self.__theme_item_g.hover_out()
                if self.__theme_item_gb.color != self.__title_label.color:
                    self.__theme_item_gb.hover_out()
                if self.__theme_item_b.color != self.__title_label.color:
                    self.__theme_item_b.hover_out()
                if self.__theme_item_rb.color != self.__title_label.color:
                    self.__theme_item_rb.hover_out()
                if self.__random_map_label.color != self.__title_label.color:
                    self.__random_map_label.hover_out()
                if self. __color_defense_label.color != self.__title_label.color:
                    self.__color_defense_label.hover_out()
                if self.__effect_ball_label.color != self.__title_label.color:
                    self.__effect_ball_label.hover_out()
                if self.__clean_scoreboard_label.color != self.__title_label.color:
                    self.__clean_scoreboard_label.hover_out()
                if self.__return_menu_label.color != self.__title_label.color:
                    self.__return_menu_label.hover_out()
            elif maybe_obj is self.__choose_theme_label or maybe_obj is self.__theme_item_r or maybe_obj is self.__theme_item_rg or maybe_obj is self.__theme_item_g or maybe_obj is self.__theme_item_gb or maybe_obj is self.__theme_item_b or maybe_obj is self.__theme_item_rb or maybe_obj is self.__random_map_label or maybe_obj is self.__color_defense_label or maybe_obj is self.__effect_ball_label or maybe_obj is self.__clean_scoreboard_label or maybe_obj is self.__return_menu_label:
                maybe_obj.hover_on()
        # page 4: scoreboard
        elif self.__page_no == 4:
            maybe_obj = self.__window.get_object_at(mouse_obj.x, mouse_obj.y)
            if maybe_obj is None:
                if self.__return_menu_label.color != self.__title_label.color:
                    self.__return_menu_label.hover_out()
            elif maybe_obj is self.__return_menu_label:
                maybe_obj.hover_on()

    def update_life_point(self):
        """
        Update life point label to display current life point left.
        """
        self.__window.remove(self.__life_point_label)
        self.__life_point_text = ""
        for i in range(self.__life_point):
            self.__life_point_text += "❤"
        self.__life_point_label.text = self.__life_point_text
        self.__window.add(self.__life_point_label, self.__window.width - self.__life_point_label.width, self.__window.height)

    def set_ball_position(self):
        """
        Set ball's position to the default on the paddle's center.
        """
        if self.__ball is not None:
            self.__ball.default_setting()
            self.__window.add(self.__ball, self.__paddle_center_x - self.__ball_width/2, self.__paddle.y - self.__ball_height)
            self.__ball_count = 1

    def set_effect_default(self):
        """
        set the effect ball and all the effecting flags to default status.
        """
        if self.__effect_ball is not None:
            self.__effect_ball.y = self.__window.height + self.__effect_ball.height
            self.__effect_ball.get_effect_label().y = self.__effect_ball.y
            self.__window.remove(self.__effect_ball)
        self.__effecting_no = 1
        self.clean_effect()
        self.__effecting = False
        self.__effect_ball_show = False
        self.__effecting_type = 0
        self.__effecting_no = 0
        self.__effect_ball_desc.text = ""
        self.__effecting_time = 0
        self.__effecting_count = 0
        self.__count_down_bar.text = ""
        if self.__have_extra_ball and not self.__clear_game:
            self.remove_extra_ball()

    def one_more_chance(self):
        """
        When losing one life point but still have chances to challenge.
        """
        self.create_ball()
        self.set_ball_position()
        self.set_effect_default()
        self.__hint_label.text = "Click to Start"
        self.__hint_label.x = self.__window.width / 2 - self.__hint_label.width / 2
        self.__hint_label.y = self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height + self.__hint_label.height * 4
        self.__game_on = False

    def game_over(self):
        """
        When losing all life then game over.
        """
        self.__game_over = True
        self.create_ball()
        self.__ball.default_setting()
        self.set_effect_default()
        self.__window.remove(self.__ball)
        self.__game_end_label.text = "GAME OVER"
        self.__game_end_label.color = (150, 0, 0)
        self.__game_end_label.x = self.__window.width / 2 - self.__game_end_label.width / 2
        self.__game_end_label.y = self.__window.height / 2 + self.__ball_height / 2 - self.__game_end_label.height
        self.__hint_label.text = "Click to Continue"
        self.__hint_label.x = self.__window.width / 2 - self.__hint_label.width / 2
        self.__hint_label.y = self.__window.height / 2 + self.__ball_height / 2 + self.__ball_height + self.__hint_label.height * 4

    def game_pause(self):
        """
        To pause the game.
        """
        self.__ball.set_speed(0)
        if self.__have_extra_ball:
            self.__extra_ball.set_speed(0)
        if self.__effect_ball_show:
            self.__effect_ball.set_speed(0)
        self.__game_pause = True

    def game_resume(self):
        """
        Unpause the game.
        """
        self.__ball.set_speed(1)
        if self.__have_extra_ball:
            self.__extra_ball.set_speed(1)
        if self.__effect_ball_show:
            self.__effect_ball.set_speed(1)
        self.__game_pause = False

    def update_scoreboard(self):
        """
        update the scoreboard if the user current score is higher than any of scores in top 5.
        """
        if self.__your_score != 0:
            if self.__your_score > self.__top_5:
                if self.__your_score > self.__top_4:
                    if self.__your_score > self.__top_3:
                        if self.__your_score > self.__top_2:
                            if self.__your_score > self.__top_1:
                                self.__new_record = True
                                self.__top_5 = self.__top_4
                                self.__top_4 = self.__top_3
                                self.__top_3 = self.__top_2
                                self.__top_2 = self.__top_1
                                self.__top_1 = self.__your_score
                            else:
                                self.__top_5 = self.__top_4
                                self.__top_4 = self.__top_3
                                self.__top_3 = self.__top_2
                                self.__top_2 = self.__your_score
                        else:
                            self.__top_5 = self.__top_4
                            self.__top_4 = self.__top_3
                            self.__top_3 = self.__your_score
                    else:
                        self.__top_5 = self.__top_4
                        self.__top_4 = self.__your_score
                else:
                    self.__top_5 = self.__your_score

    def clean_scoreboard(self):
        """
        Reset all the scores record.
        """
        self.__top_5 = 0
        self.__top_4 = 0
        self.__top_3 = 0
        self.__top_2 = 0
        self.__top_1 = 0
        self.__your_score = 0

    @staticmethod
    def switch_boolean(switch_boolean):
        """
        Like a switch action.
        """
        if switch_boolean:
            return False
        else:
            return True

    @staticmethod
    def get_boolean_icon(boolean):
        """
        Return boolean's representing icon.
        """
        if boolean:
            return "✔"
        else:
            return "✘"

    def get_window(self):
        """
        Return the GWindow in use.
        """
        return self.__window

    def get_page_no(self):
        """
        Return on what page currently.
        """
        return self.__page_no

    def get_game_on(self):
        """
        Return to know if the game is on or not.
        """
        return self.__game_on

    def get_ball(self):
        """
        Return the main ball.
        """
        return self.__ball

    def get_have_extra_ball(self):
        """
        Return if currently have an extra ball on screen.
        """
        return self.__have_extra_ball

    def get_extra_ball(self):
        """
        Return the extra ball.
        """
        return self.__extra_ball

    def get_ball_count(self):
        """
        Return how many balls on screen now.
        """
        return self.__ball_count

    def set_ball_count(self, ball_count):
        """
        Set current ball numbers.
        """
        self.__ball_count += ball_count

    def get_effect_ball(self):
        """
        Return the effect ball.
        """
        return self.__effect_ball

    def get_effect_ball_show(self):
        """
        Return if currently have an effect ball on screen.
        """
        return self.__effect_ball_show

    def set_effect_ball_show(self, effect_ball_show):
        """
        Set if currently have an effect ball or not.
        """
        self.__effect_ball_show = effect_ball_show

    def set_effect_ball_desc(self, effect_ball_desc):
        """
        Set effect ball description on screen.
        """
        self.__effect_ball_desc.text = effect_ball_desc

    def get_effecting(self):
        """
        Return if it's in effecting or now.
        """
        return self.__effecting

    def get_life_point(self):
        """
        Return current life point.
        """
        return self.__life_point

    def set_life_point(self, v_point):
        """
        Set current life point when changes.
        """
        self.__life_point += v_point

    def paddle_follow_ball(self):
        """
        Set the paddle movement follow the ball for background display.
        """
        self.__paddle.x = self.__ball.x - self.__paddle.width / 2 + self.__ball_width/2

    def set_theme_color(self, theme_r, theme_g, theme_b):
        """
        Set theme color to balls, paddle, labels accordingly.
        """
        self.__theme_r = theme_r
        self.__theme_g = theme_g
        self.__theme_b = theme_b
        self.__ball.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__title_label.color = self.__ball.color
        self.__paddle.color = self.__ball.color
        self.__paddle.fill_color = self.__ball.color
        self.__start_game_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__game_setting_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__score_board_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__exit_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__return_menu_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__choose_theme_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__random_map_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__color_defense_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__effect_ball_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__clean_scoreboard_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__pause_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__quit_label.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__theme_item_r.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__theme_item_rg.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__theme_item_g.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__theme_item_gb.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__theme_item_b.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)
        self.__theme_item_rb.set_theme_color(self.__theme_r, self.__theme_g, self.__theme_b)

    def change_random_color(self):
        """
        change color in random.
        """
        self.__ball.random_color()
        self.__title_label.color = self.__ball.color
        self.__paddle.color = self.__ball.color
        self.__paddle.fill_color = self.__ball.color

    def get_brick_nums(self):
        """
        Return current brick numbers.
        """
        return self.__brick_nums


class GBrick(GRect):
    """
    A brick instance extends from GRect, with new attributes and methods.
    """
    def __init__(self, width, height, *, x=0, y=0, row=0, brick_lvl_lst=DEFAULT_BRICK_LVL_LST, theme_r=DEFAULT_THEME_R, theme_g=DEFAULT_THEME_G, theme_b=DEFAULT_THEME_B, color_defense_on=False):
        super().__init__(width, height, x=x, y=y)
        self.__have_effect_ball = random.randint(1, 2)
        # decide this brick' levels(life point).
        self.__brick_lvl_lst = brick_lvl_lst
        if not color_defense_on:
            self.__brick_life_default = 1
        else:
            for i in range(len(self.__brick_lvl_lst)):
                for j in range(len(self.__brick_lvl_lst[i])):
                    if row == self.__brick_lvl_lst[i][j]:
                        self.__brick_life_default = i + 1

        if self.__brick_life_default == 1:  # light theme color
            self.__brick_r = self.light_theme_color(theme_r)
            self.__brick_g = self.light_theme_color(theme_g)
            self.__brick_b = self.light_theme_color(theme_b)
        elif self.__brick_life_default == 2:  # original theme color
            self.__brick_r = theme_r
            self.__brick_g = theme_g
            self.__brick_b = theme_b
        else:  # dark theme color
            self.__brick_r = self.dark_theme_color(theme_r)
            self.__brick_g = self.dark_theme_color(theme_g)
            self.__brick_b = self.dark_theme_color(theme_b)

        self.__brick_life = self.__brick_life_default
        self.__point = 10 + 10 * (self.__brick_life_default - self.__brick_life)
        self.filled = True
        self.fill_color = (self.__brick_r, self.__brick_g, self.__brick_b)
        self.color = (self.__brick_r, self.__brick_g, self.__brick_b)

    def have_effect_ball(self):
        """
        Return if this brick contains effect ball.
        """
        return self.__have_effect_ball == 1

    def remove_brick(self):
        """
        The brick methods to decide whether this brick will be removed or not.
        If the brick remains life point, changing the brick color accordingly.
        """
        if self.__brick_life == 2:
            self.__brick_r = self.origin_theme_color(self.__brick_r)
            self.__brick_g = self.origin_theme_color(self.__brick_g)
            self.__brick_b = self.origin_theme_color(self.__brick_b)
            self.fill_color = (self.__brick_r, self.__brick_g, self.__brick_b)
            self.color = (self.__brick_r, self.__brick_g, self.__brick_b)
            return False
        elif self.__brick_life == 1:
            self.__brick_r = self.light_theme_color(self.__brick_r)
            self.__brick_g = self.light_theme_color(self.__brick_g)
            self.__brick_b = self.light_theme_color(self.__brick_b)
            self.fill_color = (self.__brick_r, self.__brick_g, self.__brick_b)
            self.color = (self.__brick_r, self.__brick_g, self.__brick_b)
            return False
        else:
            return True

    def set_brick_life(self, v_life, power_ball_mode_on):
        """
        Update the brick life, if the power ball mode on, the brick life directly turn to zero.
        """
        if power_ball_mode_on:
            self.__brick_life = 0
        else:
            self.__brick_life += v_life

    def get_point(self, power_ball_mode_on):
        """
        Return the point of this brick, if the power ball mode on, return all collected points.
        """
        if power_ball_mode_on:
            for i in range(self.__brick_life):
                self.__point = 10 + 10 * i
        return self.__point

    @staticmethod
    def dark_theme_color(rgb):
        """
        Turn to dark theme color RGB.
        """
        if 100 <= rgb < 255:
            rgb -= 100
        return rgb

    @staticmethod
    def light_theme_color(rgb):
        """
        Turn to light theme color RGB.
        """
        if rgb <= 105:
            rgb += 150
        return rgb

    @staticmethod
    def origin_theme_color(rgb):
        """
        Turn to original theme color RGB.
        """
        if rgb != 0:
            rgb += 100
        return rgb


class GBall(GOval):
    """
    A ball instance extends from GOval, with new attributes and methods.
    """
    def __init__(self, width, height, *, x=0, y=0):
        super().__init__(width, height, x=x, y=y)
        self.__dx = 0
        self.__dy = 0
        self.__dx_default = 0
        self.__dy_default = 0
        self.__background_x = 0
        self.__background_y = 0

    def initial_velocity(self):
        """
        Initial the velocity to make ball move.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = -INITIAL_Y_SPEED
        self.__dx_default = self.__dx
        self.__dy_default = self.__dy

    def follow_velocity(self, follow_dx):
        """
        Follow the current ball on screen in opposite x-directions.
        """
        self.__dx = -follow_dx
        self.__dy = -INITIAL_Y_SPEED
        self.__dx_default = self.__dx
        self.__dy_default = self.__dy

    def get_dx(self):
        """
        Return this ball's x-pace.
        """
        return self.__dx

    def get_dy(self):
        """
        Return this ball's y-pace.
        """
        return self.__dy

    def bounce_dx(self):
        """
        Set x-directions change when bouncing.
        """
        self.__dx *= -1
        self.__dx_default *= -1

    def bounce_dy(self):
        """
        Set y-directions change when bouncing.
        """
        self.__dy *= -1
        self.__dy_default *= -1

    def set_speed(self, scale):
        """
        Set the speed of movement by scale, if scale is 1, stay the same speed of original.
        """
        if scale == 1:
            self.__dx = self.__dx_default
            self.__dy = self.__dy_default
        else:
            self.__dx *= scale
            self.__dy *= scale

    def default_setting(self):
        """
        Default all the movement setting.
        """
        self.__dx = 0
        self.__dy = 0
        self.__dx_default = 0
        self.__dy_default = 0

    def random_color(self):
        """
        Change ball's color in random.
        """
        __random_r = random.randint(50, 200)
        __random_g = random.randint(50, 200)
        __random_b = random.randint(50, 200)
        self.fill_color = (__random_r, __random_g, __random_b)
        self.color = (__random_r, __random_g, __random_b)

    def set_theme_color(self, theme_r, theme_g, theme_b):
        """
        Set this ball's color accordingly to the theme color.
        """
        self.fill_color = (theme_r, theme_g, theme_b)
        self.color = (theme_r, theme_g, theme_b)

    def get_background_x(self):
        """
        If this ball is bouncing on background, get it's x position when change to another pages.
        """
        return self.__background_x

    def get_background_y(self):
        """
        If this ball is bouncing on background, get it's y position when change to another pages.
        """
        return self.__background_y

    def set_background_xy(self, x, y):
        """
        If this ball is bouncing on background, set it's position before change to another pages.
        """
        self.__background_x = x
        self.__background_y = y


class GEffectBall(GOval):
    """
    An effect ball instance extends from GOval, with new attributes and methods.
    """
    def __init__(self, width, height, *, x=0, y=0, have_extra_ball=False):
        super().__init__(width, height, x=x, y=y)
        """
        GPaddle effect_type controls the effect type.
        effect_type = 1 : effect for paddle
        effect_type = 2 : effect for ball
        effect_type = 3 : effect for brick (power ball makes brick no defense)
        effect_type = 4 : effect for gains
        """
        self.__effect_type = 0
        self.__effect_no = 0
        self.__effect_label = GLabel("?")
        self.__effect_label.color = (255, 255, 255)
        self.__effect_desc = "Is it good to drink?"
        self.__random_uncovered = random.randint(1, 6)
        self.__ball_r = 150
        self.__ball_g = 0
        self.__ball_b = 150
        self.__have_extra_ball = have_extra_ball
        self.__effect_time = 0
        self.initial_effect_ball()
        self.__dy = random.randint(1, 3)
        self.__dy_default = self.__dy

    def initial_effect_ball(self):
        self.__effect_type = random.randint(1, 4)
        if self.__effect_type == 1:  # paddle effect
            """
            effect_type = 1 : paddle effect
            effect_no = 1 : default setting
            effect_no = 2 : W, widen the paddle to 2x
            effect_no = 3 : N, narrow the paddle to 0.5x
            """
            self.__effect_no = random.randint(2, 3)
            if self.__random_uncovered != 1:
                self.__ball_r = 0
                self.__ball_g = 150
                self.__ball_b = 0
                if self.__effect_no == 2:
                    self.__effect_label.text = "W"  # widen the paddle
                    self.__effect_desc = "Wide the paddle!!"
                elif self.__effect_no == 3:
                    self.__effect_label.text = "N"  # narrow the paddle
                    self.__effect_desc = "Narrow the paddle.."
        elif self.__effect_type == 2:  # ball effect
            """
            effect_type = 2 : ball effect
            effect_no = 1 : default setting
            effect_no = 2 : F, fasten the ball
            effect_no = 3 : S, slow down the ball
            """
            self.__effect_no = random.randint(2, 3)
            if self.__random_uncovered != 1:
                self.__ball_r = 150
                self.__ball_g = 150
                self.__ball_b = 0
                if self.__effect_no == 2:
                    self.__effect_label.text = "F"  # fasten the ball
                    self.__effect_desc = "Fasten the ball!!"
                elif self.__effect_no == 3:
                    self.__effect_label.text = "S"  # slow down the ball
                    self.__effect_desc = "Slow down the ball.."
        elif self.__effect_type == 3:  # brick effect
            """
            effect_type = 3 : brick effect (power ball makes brick no defense)
            effect_no = 1 : default setting
            effect_no = 2 : P, power ball go through the bricks
            """
            self.__effect_no = random.randint(2, 2)
            if self.__random_uncovered != 1:
                self.__ball_r = 0
                self.__ball_g = 150
                self.__ball_b = 150
                if self.__effect_no == 2:
                    self.__effect_label.text = "P"  # power ball go through the bricks
                    self.__effect_desc = "Hey, It's Power Ball!!"
        elif self.__effect_type == 4:  # gain effect
            """
            effect_type = 4 : gains effect
            effect_no = 1 : ❤, gain one life point
            effect_no = 2 : ⦿, gain another ball
            """
            if self.__have_extra_ball:
                self.__effect_no = random.randint(1, 1)
            else:
                self.__effect_no = random.randint(1, 2)
            if self.__random_uncovered != 1:
                self.__ball_r = 150
                self.__ball_g = 0
                self.__ball_b = 0
                if self.__effect_no == 1:
                    self.__effect_label.text = "❤"  # gain one life point
                    self.__effect_desc = "Please catch my heart."
                elif self.__effect_no == 2:
                    self.__effect_label.text = "⦿"  # gain another ball
                    self.__effect_desc = "We need more allies!"
        self.filled = True
        self.fill_color = (self.__ball_r, self.__ball_g, self.__ball_b)
        self.color = (self.__ball_r, self.__ball_g, self.__ball_b)
        if self.__effect_type != 4:
            self.__effect_time = random.randint(5, 10)

    def get_dy(self):
        """
        Return this effect ball's x-pace.
        """
        return self.__dy

    def get_effect_type(self):
        """
        Return this effect ball's effect type.
        """
        return self.__effect_type

    def get_effect_no(self):
        """
        Return this effect ball's effect no.
        """
        return self.__effect_no

    def get_effect_time(self):
        """
        Return this effect ball's effect time.
        """
        return self.__effect_time

    def get_effect_label(self):
        """
        Return this effect ball's effect label.
        """
        return self.__effect_label

    def get_effect_label_x(self):
        """
        Return the x position of the effect label.
        """
        return self.x + self.width/2 - self.__effect_label.width/2.5

    def get_effect_label_y(self):
        """
        Return the y position of the effect label.
        """
        return self.y + self.height - self.height/2 + self.__effect_label.height/1.5

    def get_effect_desc(self):
        """
        Return this effect ball's effect description.
        """
        return self.__effect_desc

    def set_speed(self, scale):
        """
        Set the speed of movement by scale, if scale is 1, stay the same speed of original.
        """
        if scale == 1:
            self.__dy = self.__dy_default
        else:
            self.__dy *= scale


class GItem(GLabel):
    """
    A label select item instance extends from GLabel, with new attributes and methods.
    """
    def __init__(self, label, x=0, y=0, font_size=15):
        super().__init__(label, x=x, y=y)
        self.__label_text = label
        self.font = "Verdana-" + str(font_size)
        self.__item_r = 100
        self.__item_g = 100
        self.__item_b = 100
        self.__on_item_r = 0
        self.__on_item_g = 0
        self.__on_item_b = 150
        self.color = (self.__item_r, self.__item_g, self.__item_b)

    def hover_on(self):
        """
        Set the color and text when mouse hover on item.
        """
        self.color = (self.__on_item_r, self.__on_item_g, self.__on_item_b)
        self.text = self.__label_text + "   ☜"

    def hover_on_no_hand(self):
        """
        Set only the color when mouse hover on item.
        """
        self.color = (self.__on_item_r, self.__on_item_g, self.__on_item_b)

    def hover_out(self):
        """
        Set the color and text when mouse hover out item.
        """
        self.color = (self.__item_r, self.__item_g, self.__item_b)
        self.text = self.__label_text

    def hover_out_no_hand(self):
        """
        Set only the color when mouse hover out item.
        """
        self.color = (200, 200, 200)

    def set_theme_color(self, theme_r, theme_g, theme_b):
        """
        Set this item's color accordingly to the theme color.
        """
        self.__on_item_r = theme_r
        self.__on_item_g = theme_g
        self.__on_item_b = theme_b

    def set_label_text(self, label_text):
        """
        Set the label's text.
        """
        self.__label_text = label_text
        self.text = self.__label_text


class GOvalItem(GOval):
    """
    An oval select item instance extends from GOval, with new attributes and methods.
    """
    def __init__(self, width, height, *, x=0, y=0, r=0, g=0, b=150):
        super().__init__(width, height, x=x, y=y)

        self.__r = 100
        self.__g = 100
        self.__b = 100
        self.__item_r = r
        self.__item_g = g
        self.__item_b = b
        self.__on_r = DEFAULT_THEME_R
        self.__on_g = DEFAULT_THEME_G
        self.__on_b = DEFAULT_THEME_B

        self.filled = True
        self.color = (self.__r, self.__g, self.__b)
        self.fill_color = (self.__r, self.__g, self.__b)
        self.__item = GOval(width * 0.8, height * 0.8)
        self.__item.filled = True
        self.__item.fill_color = (self.__item_r, self.__item_g, self.__item_b)
        self.__item.color = (self.__item_r, self.__item_g, self.__item_b)

    def hover_on(self):
        """
        Set the color and text when mouse hover on oval item.
        """
        self.color = (self.__on_r, self.__on_g, self.__on_b)
        self.fill_color = (self.__on_r, self.__on_g, self.__on_b)

    def hover_out(self):
        """
        Set the color and text when mouse hover out oval item.
        """
        self.color = (self.__r, self.__g, self.__b)
        self.fill_color = (self.__r, self.__g, self.__b)

    def set_theme_color(self, theme_r, theme_g, theme_b):
        """
        Set this oval item's color accordingly to the theme color.
        """
        self.__on_r = theme_r
        self.__on_g = theme_g
        self.__on_b = theme_b

    def get_item_r(self):
        """
        Return this oval item' RGB as theme color.
        """
        return self.__item_r

    def get_item_g(self):
        """
        Return this oval item' RGB as theme color.
        """
        return self.__item_g

    def get_item_b(self):
        """
        Return this oval item' RGB as theme color.
        """
        return self.__item_b

    def get_item(self):
        """
        Return this oval item as select item.
        """
        return self.__item

    def get_item_x(self):
        """
        Return this oval item's x position.
        """
        return self.x + (self.width - self.__item.width)/2

    def get_item_y(self):
        """
        Return this oval item's y position.
        """
        return self.y + (self.height - self.__item.height)/2

