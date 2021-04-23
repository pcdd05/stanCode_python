"""
File: my_drawing
Name: DiCheng
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
import random

# This constant determines the size of rocket and window size, recommended from SIZE 5~8 to get the best drawing.
SIZE = 7
# This constant controls each pixel size.
PIXEL_SIZE = 10

# These constants control the hill's color.
HILL_R = 249
HILL_G = 223
HILL_B = 192

# These constants control the color both of head of rocket and the tail of rocket.
HEAD_R = 230
HEAD_G = 0
HEAD_B = 0

# These constants control the color of body of rocket.
BODY_R = 112
BODY_G = 128
BODY_B = 144

# This global variable create a GWindow instance.
window = GWindow(SIZE*100, SIZE*150)
# This global variable control the rocket position in the center of window.
center_x = window.width // 2

# These global variable control the edge of painting objects.
first_x = 0
last_x = 0
last_y = window.height - window.height//5*2 - 6 * SIZE * PIXEL_SIZE + 3 * PIXEL_SIZE


def main():
    """
    Design idea:
    This rocket is an upgrade version from SC001>Assignment3>rocket.py, I give you-- ROCKET 2.0!!

    Description:
    Other than using SIZE param to build a different size of rocket,
    ROCKET 2.0 is set up in random location each time,
    hard to believe it?
    just focus on faraway small hills, and stars on the sky each time execute the program. ;)
    """
    paint_background()
    draw_rocket_head()
    draw_rocket_belt()
    # to build a bigger rocket!
    for i in range(2):
        draw_rocket_upper()
        draw_rocket_lower()
    draw_rocket_belt()
    draw_rocket_head()
    add_stars()


def paint_background():
    """
    paint the location where rocket will be set up, the dark sky, the bisque-colored ground and the random hills.
    """
    black_rgb = 0
    brown_r = 255
    brown_g = 228
    brown_b = 196
    draw_hill = True
    for y in range(0, window.height, PIXEL_SIZE):
        # sky
        if y <= window.height//5*3:
            black_rgb = check_rgb(black_rgb + 255 // (window.height//5*3 // PIXEL_SIZE))
            sky_rect = GRect(window.width, PIXEL_SIZE)
            sky_rect.filled = True
            sky_rect.fill_color = (black_rgb, black_rgb, black_rgb)
            sky_rect.color = (black_rgb, black_rgb, black_rgb)
            window.add(sky_rect, 0, y)
        # ground
        else:
            if draw_hill is True:
                # hills
                draw_background_hill(random.randint(2, 9), y)
                draw_hill = False
            brown_r = check_rgb(brown_r - brown_r // (window.height//5*2 // PIXEL_SIZE))
            brown_g = check_rgb(brown_g - brown_g // (window.height//5*2 // PIXEL_SIZE))
            brown_b = check_rgb(brown_b - brown_b // (window.height//5*2 // PIXEL_SIZE))
            ground_rect = GRect(window.width, PIXEL_SIZE)
            ground_rect.filled = True
            ground_rect.fill_color = (brown_r, brown_g, brown_b)
            ground_rect.color = (brown_r, brown_g, brown_b)
            window.add(ground_rect, 0, y)


def draw_background_hill(hill_num, surface_y):
    """
    draw random hills, random numbers of hill and random locations.
    """
    hill_bottom_x_start = random.randint(0, window.width//hill_num)
    for i in range(hill_num):
        random_hill_height = random.randint(3, 9) * PIXEL_SIZE
        hill_wide = 2*random_hill_height
        for h in range(random_hill_height // PIXEL_SIZE):
            for w in range(h*2):
                hill_square = GRect(PIXEL_SIZE, PIXEL_SIZE)
                hill_square.filled = True
                hill_square.fill_color = (HILL_R, HILL_G, HILL_B)
                hill_square.color = (HILL_R, HILL_G, HILL_B)
                window.add(hill_square, (hill_bottom_x_start + hill_wide) // 2 - h*PIXEL_SIZE + w*PIXEL_SIZE, (surface_y - random_hill_height) + h*PIXEL_SIZE)
        if i + 1 < hill_num:
            if hill_bottom_x_start + hill_wide > window.width:
                hill_bottom_x_start = 0
            hill_bottom_x_start = random.randint(hill_bottom_x_start + hill_wide, ((window.width - (hill_bottom_x_start + hill_wide))//(hill_num - (i+1)) + hill_bottom_x_start + hill_wide))


def draw_rocket_head():
    """
    draw rocket head, rocket tail as well, with layered color painted.
    """
    global first_x, last_x, last_y
    head_y = last_y
    for i in range(SIZE+5):
        for j in range(i*2):
            draw_square(center_x - i*PIXEL_SIZE + j*PIXEL_SIZE, head_y+i*PIXEL_SIZE)
    paint_color_layered(HEAD_R, HEAD_G, HEAD_B, first_x, last_x, head_y, last_y)


def draw_rocket_belt():
    """
    draw rocket belt with magenta light balls on both side.
    """
    global last_y
    belt_y = last_y + PIXEL_SIZE
    col = 2 * (SIZE + 1)
    for i in range(1):
        draw_circle(255, 0, 255, center_x - (col // 2)*PIXEL_SIZE, belt_y)
    for j in range(col - 2):
        draw_square(center_x - (col // 2)*PIXEL_SIZE + PIXEL_SIZE + j*PIXEL_SIZE, belt_y)
    paint_color_layered(BODY_R, BODY_G, BODY_B, center_x - (col // 2)*PIXEL_SIZE, center_x + (col // 2)*PIXEL_SIZE - PIXEL_SIZE, last_y, last_y)
    for i in range(1):
        draw_circle(255, 0, 255, center_x + (col // 2)*PIXEL_SIZE - PIXEL_SIZE, belt_y)


def draw_rocket_upper():
    """
    draw rocket upper part, with layered color painted.
    """
    global first_x, last_x, last_y
    upper_y = last_y + PIXEL_SIZE
    col = 2 * (SIZE + 1)
    for i in range(SIZE):
        for j in range(1):
            draw_square(center_x - (col // 2) * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for k in range(SIZE - i - 1):
            draw_circle(224, 255, 255, center_x - (col // 2) * PIXEL_SIZE + PIXEL_SIZE + k * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for m in range(i + 1):
            draw_square(center_x - (col // 2) * PIXEL_SIZE + PIXEL_SIZE + k * PIXEL_SIZE + PIXEL_SIZE + m * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for m in range(i + 1):
            draw_square(center_x + (col // 2) * PIXEL_SIZE - PIXEL_SIZE - k * PIXEL_SIZE - 2*PIXEL_SIZE - m * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for k in range(SIZE - i - 1):
            draw_circle(224, 255, 255, center_x + (col // 2) * PIXEL_SIZE - 2*PIXEL_SIZE - k * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for j in range(1):
            draw_square(center_x + (col // 2)*PIXEL_SIZE - PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
    paint_color_layered(BODY_R, BODY_G, BODY_B,  first_x, last_x, upper_y, last_y)


def draw_rocket_lower():
    """
    draw rocket lower part, with layered color painted.
    """
    global first_x, last_x, last_y
    upper_y = last_y + PIXEL_SIZE
    col = 2 * (SIZE + 1)
    for i in range(SIZE):
        for j in range(1):
            draw_square(center_x - (col // 2) * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for k in range(i):
            draw_circle(250, 250, 210, center_x - (col // 2) * PIXEL_SIZE + PIXEL_SIZE + k * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for m in range(SIZE - i):
            draw_square(center_x - (col // 2) * PIXEL_SIZE + PIXEL_SIZE + i * PIXEL_SIZE + PIXEL_SIZE + m * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for m in range(SIZE - i):
            draw_square(center_x + (col // 2) * PIXEL_SIZE - PIXEL_SIZE - i * PIXEL_SIZE - 2*PIXEL_SIZE - m * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for k in range(i):
            draw_circle(250, 250, 210, center_x + (col // 2) * PIXEL_SIZE - 2*PIXEL_SIZE - k * PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
        for j in range(1):
            draw_square(center_x + (col // 2)*PIXEL_SIZE - PIXEL_SIZE, upper_y+i*PIXEL_SIZE)
    paint_color_layered(BODY_R, BODY_G, BODY_B,  first_x, last_x, upper_y, last_y)


def draw_square(x, y):
    """
    draw a square and add to window on given (x, y)
    """
    square = GRect(PIXEL_SIZE, PIXEL_SIZE)
    window.add(square, x, y)
    update_x_y_boundary(x, y)


def draw_circle(r, g, b, x, y):
    """
    draw a circle and add to window on given (x, y), painting with given color.
    """
    circle = GOval(PIXEL_SIZE, PIXEL_SIZE)
    circle.filled = True
    circle.fill_color = (r, g, b)
    circle.color = (r, g, b)
    window.add(circle, x, y)
    update_x_y_boundary(x, y)


def paint_color_layered(r, g, b, from_x, to_x, from_y, to_y):
    """
    paint the given color rgb layered from left side to right side.
    """
    paint_r = r
    paint_g = g
    paint_b = b
    for x in range((to_x - from_x) // PIXEL_SIZE + 1):
        paint_r = check_rgb(paint_r + (210 - r) // ((last_x - first_x) // PIXEL_SIZE))
        paint_g = check_rgb(paint_g + (210 - g) // ((last_x - first_x) // PIXEL_SIZE))
        paint_b = check_rgb(paint_b + (210 - b) // ((last_x - first_x) // PIXEL_SIZE))
        for y in range((to_y - from_y)//PIXEL_SIZE + 1):
            get_x = from_x + x*PIXEL_SIZE
            get_y = from_y + y*PIXEL_SIZE
            paint_obj = window.get_object_at(get_x, get_y)
            if paint_obj is not None and paint_obj.width == PIXEL_SIZE:
                paint_obj.fill_color = (paint_r, paint_g, paint_b)
                paint_obj.color = (paint_r, paint_g, paint_b)
    reset_x()


def check_rgb(rgb):
    """
    check if the rgb is in legal range.
    """
    if rgb >= 255:
        return 255
    if rgb <= 0:
        return 0
    return rgb


def add_stars():
    """
    adding stars on the sky.
    """
    star_num = SIZE
    star_x_start = 0
    star_x_end = window.width
    star_y_start = 0
    star_y_end = window.height - window.height//5*2 - 6 * SIZE * PIXEL_SIZE + 3 * PIXEL_SIZE
    for i in range(star_num):
        random_x = random.randint(star_x_start + PIXEL_SIZE, star_x_end - PIXEL_SIZE)
        random_y = random.randint(star_y_start + PIXEL_SIZE, star_y_end - PIXEL_SIZE)
        for x in range(3):
            for y in range(3):
                # build a star in "+" shaped.
                if (x == 0 and y == 0) or (x == 2 and y == 0) or (x == 0 and y == 2) or (x == 2 and y == 2):
                    pass
                else:
                    star = GRect(PIXEL_SIZE//2, PIXEL_SIZE//2)
                    star.filled = True
                    star.color = (240, 230, 140)
                    star.fill_color = (240, 230, 140)
                    window.add(star, random_x + (x - 1)*PIXEL_SIZE, random_y + (y - 1)*PIXEL_SIZE)


def reset_x():
    """
    reset global variable first_x and last_x to 0.
    """
    global first_x, last_x
    first_x = 0
    last_x = 0


def update_x_y_boundary(x, y):
    """
    update x and y while drawing objects.
    """
    set_first_x(x)
    set_last_x(x)
    set_last_y(y)


def set_first_x(x):
    """
    set the left edge of objects.
    """
    global first_x
    if first_x == 0:
        first_x = x
    first_x = find_min(first_x, x)


def set_last_x(x):
    """
    set the right edge of objects.
    """
    global last_x
    last_x = find_max(last_x, x)


def set_last_y(y):
    """
    set the bottom edge of objects.
    """
    global last_y
    last_y = find_max(last_y, y)


def find_min(a, b):
    """
    return smaller value.
    """
    if a < b:
        return a
    return b


def find_max(a, b):
    """
    return bigger value.
    """
    if a > b:
        return a
    return b


if __name__ == '__main__':
    main()
