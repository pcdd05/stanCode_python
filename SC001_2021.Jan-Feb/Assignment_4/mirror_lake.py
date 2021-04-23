"""
File: mirror_lake.py
Name: DiCheng
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    Using pixel coordinates to get reflection position and paint with rgb.
    :param filename: str, given file path for getting image object.
    :return: SimpleImage, the image which have its own reflection.
    """
    ori_img = SimpleImage(filename)
    result_img = SimpleImage.blank(ori_img.width, ori_img.height * 2)
    for x in range(ori_img.width):
        for y in range(ori_img.height):
            ori_img_pixel = ori_img.get_pixel(x, y)
            result_pixel_same = result_img.get_pixel(x, y)
            result_pixel_reflect = result_img.get_pixel(x, result_img.height - 1 - y)
            # assign rgb
            reassign_rgb_from_pixel(result_pixel_same, ori_img_pixel)
            reassign_rgb_from_pixel(result_pixel_reflect, ori_img_pixel)
    return result_img


def reassign_rgb_from_pixel(result_pixel, from_pixel):
    """
    given two pixel for reassign one's rgb from the other's.
    :param result_pixel: Pixel, the result pixel which were reassign the rgb.
    :param from_pixel: Pixel, the pixel which will be extracted its rgb value.
    """
    result_pixel.red = from_pixel.red
    result_pixel.green = from_pixel.green
    result_pixel.blue = from_pixel.blue


def main():
    """
    get a picture and reflect in horizontal.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
