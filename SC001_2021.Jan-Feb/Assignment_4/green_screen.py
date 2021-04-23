"""
File: green_screen.py
Name: DiCheng
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    Finding the green pixel of figure image and then replace by background pixel.
    :param background_img: SimpleImage, the image of background.
    :param figure_img: SimpleImage, the image of figure.
    :return: SimpleImage, the figure image with all green pixel replace by background image.
    """
    background_img.make_as_big_as(figure_img)

    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_pixel = figure_img.get_pixel(x, y)
            if figure_pixel.green > max(figure_pixel.red, figure_pixel.blue) * 2:
                background_pixel = background_img.get_pixel(x, y)
                figure_pixel.red = background_pixel.red
                figure_pixel.green = background_pixel.green
                figure_pixel.blue = background_pixel.blue
    return figure_img


def main():
    """
    get a figure image and replace the green pixels by space ship image.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
