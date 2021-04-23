"""
File: shrink.py
Name: DiCheng
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    Using pixel coordinates to get the pixel and its 2x2 neighbors for average of rgb and then paint on the small image.
    :param filename: str, given file path for getting image object.
    :return SimpleImage, the image which were been shrink to 1/2 size.
    """
    big_img = SimpleImage(filename)
    small_img = SimpleImage.blank(big_img.width // 2, big_img.height // 2)
    for x in range(small_img.width):
        for y in range(small_img.height):
            assign_shrink_rgb(big_img, small_img, x, y)
    return small_img


def assign_shrink_rgb(big_img, small_img, x, y):
    """
    Getting the target pixel and its 2x2 neighbors' rgb average then paint on the small image.
    :param big_img: SimpleImage, the image of original size.
    :param small_img: SimpleImage, the image will shrink to 1/2 size.
    :param x: int, the x coordinate which indicate the location of pixel which is starting point for 2x2 square.
    :param y: int, the y coordinate which indicate the location of pixel which is starting point for 2x2 square.
    """
    total_red = 0
    total_green = 0
    total_blue = 0
    for i in range(2):
        for j in range(2):
            total_red += big_img.get_pixel(x * 2 + i, y * 2 + j).red
            total_green += big_img.get_pixel(x * 2 + i, y * 2 + j).green
            total_blue += big_img.get_pixel(x * 2 + i, y * 2 + j).blue
    small_img_pixel = small_img.get_pixel(x, y)
    small_img_pixel.red = total_red // 2 ** 2
    small_img_pixel.green = total_green // 2 ** 2
    small_img_pixel.blue = total_blue // 2 ** 2


def main():
    """
    get a picture and shrink it to 1/2 size.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
