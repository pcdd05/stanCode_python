"""
File: draw_line.py
Name: DiCheng
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine, GLabel, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousemoved

# This constant controls the size of the circle and the font size of clean_button.
SIZE = 10
# This constant represent for color black.
BLACK = "black"
# This constant represent for color red.
RED = "red"
# This global variable create a GWindow instance.
window = GWindow()
# This global variable create a GOval instance.
circle = GOval(SIZE, SIZE)
# This global variable controls next click is draw a line or not.
next_click_draw_line = False

# extension: This global variable create a GLabel instance for showing coordinate.
coordinate_label = GLabel("")
# extension: This global variable create a GLabel instance for showing clean button.
clean_button = GLabel("Clean Canvas")
# extension: Set attribute to clean_button font at global zone is for button_frame referring to the size.
clean_button.font = "Verdana-" + str(SIZE+5)
# extension: This global variable create a GRect instance for making a frame for button.
button_frame = GRect(clean_button.width*1.2, clean_button.height*1.2)
# extension: This global variable controls is clean button exist on window or not.
exist_clean_button = False


def main():
    """
    This program will prepare canvas for drawing circle and line,
    while listening to onmouseclicked and onmousemove events.
    """
    prepare_canvas()
    onmouseclicked(click_event)
    onmousemoved(move_event)


def prepare_canvas():
    """
    Preparing canvas, setting variables to default value and adding coordinate_label for mouse move_event.
    """
    global next_click_draw_line, exist_clean_button
    circle.color = BLACK
    next_click_draw_line = False
    exist_clean_button = False
    window.add(coordinate_label)


def click_event(mouse_obj):
    """
    When user click mouse,
    depends on whether is click on clean button or not, functions will do drawing or do cleaning.
    :param mouse_obj: class, a GMouseEvent instance to indicate where the user's mouse is.
    """
    if window.get_object_at(mouse_obj.x, mouse_obj.y) is not clean_button:
        circle_to_line(mouse_obj)
    else:
        clean_canvas()


def circle_to_line(mouse_obj):
    """
    When user click mouse,
    this function will determined whether to draw a circle spot or to draw a line by is_draw_line.
    :param mouse_obj: class, a GMouseEvent instance to indicate where the user's mouse is.
    """
    global next_click_draw_line
    if next_click_draw_line:
        line = GLine(circle.x + circle.width/2, circle.y + circle.height/2, mouse_obj.x, mouse_obj.y)
        window.add(line)
        window.remove(circle)
        next_click_draw_line = False
    else:
        window.add(circle, mouse_obj.x - circle.width/2, mouse_obj.y - circle.height/2)
        next_click_draw_line = True
    if not exist_clean_button:
        show_clean_button()


def show_clean_button():
    """
    extension:
    adding clean_button and button_frame instances to window.
    """
    global exist_clean_button
    button_frame.color = BLACK
    window.add(button_frame, window.width - button_frame.width - 1, 0)
    window.add(clean_button, button_frame.x + 1 + (button_frame.width - clean_button.width) / 2, clean_button.height + (button_frame.height - clean_button.height)/2)
    exist_clean_button = True


def clean_canvas():
    """
    extension:
    clear any instances attached on window, and then prepare new canvas.
    """
    window.clear()
    prepare_canvas()


def move_event(mouse_obj):
    """
    extension:
    When user move mouse,
    this function will get the mouse coordinate and set attribute to different instance in different conditions.
    :param mouse_obj: class, a GMouseEvent instance to indicate where the user's mouse is.
    """
    if 0 <= mouse_obj.x <= window.width and 0 <= mouse_obj.y <= window.height:
        if window.get_object_at(mouse_obj.x, mouse_obj.y) is clean_button:
            coordinate_label.text = ""
            button_frame.color = RED
            clean_button.color = RED
        else:
            coordinate_label.text = get_coordinate_text(mouse_obj.x, mouse_obj.y)
            coordinate_label.x = mouse_obj.x
            coordinate_label.y = mouse_obj.y
            # in order to let coordinate_label to be seen clearly, set coordinate in particular positions.
            if mouse_obj.x + coordinate_label.width >= window.width:
                coordinate_label.x = window.width - coordinate_label.width
            if mouse_obj.y - coordinate_label.height < 0:
                coordinate_label.y = coordinate_label.height
            # if mouse_obj.x < 0:
            #     coordinate_label.x = 0
            # if mouse_obj.y > window.height:
            #     coordinate_label.y = window.height
            if clean_button.color != circle.color:
                button_frame.color = BLACK
                clean_button.color = BLACK
    else:
        coordinate_label.text = ""


def get_coordinate_text(x, y):
    """
    extension:
    Get the x-coordinate and y-coordinate of mouse and return string coordinate.
    :param x: The x-coordinate of the mouse.
    :param y: The y-coordinate of the mouse.
    :return str, the string of coordinate.
    """
    return "(" + str(x) + "," + str(y) + ")"



if __name__ == "__main__":
    main()
