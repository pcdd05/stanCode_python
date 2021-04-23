"""
File: fire.py
Name: DiCheng
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

# the factor for identify the rgb of fire.
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    Using the HURDLE_FACTOR to identify pixel which might be fire and give a real red to highlight, otherwise paint gray.
    :param filename: str, given file path for getting image object.
    :return: SimpleImage, the image which were highlighted the fires spots.
    """
    greenland_fire_img = SimpleImage(filename)
    for pixel in greenland_fire_img:
        if pixel.red > (pixel.red + pixel.green + pixel.blue) // 3 * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = (pixel.red + pixel.green + pixel.blue) // 3
            pixel.green = (pixel.red + pixel.green + pixel.blue) // 3
            pixel.blue = (pixel.red + pixel.green + pixel.blue) // 3
    return greenland_fire_img


def main():
    """
    get a picture and highlight where may spot fires in real red.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
