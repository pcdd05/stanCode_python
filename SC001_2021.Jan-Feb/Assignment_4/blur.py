"""
File: blur.py
Name: DiCheng
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Using pixel coordinates to get the pixel and its neighbors for average of rgb and then get blurred.
    :param img: SimpleImage, the image object which will be blurred.
    :return: SimpleImage, the image which were all blurred.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            assign_avg_rgb_from_neighbor(img, new_img, x, y)
    return new_img


def assign_avg_rgb_from_neighbor(old_img, new_img, ori_x, ori_y):
    """
    Getting the target pixel and its neighbors' rgb average then blur target pixel.
    :param old_img: SimpleImage, the image before blurred.
    :param new_img: SimpleImage, the image will be painted by blurred pixels.
    :param ori_x: int, the x coordinate which indicate the location of pixel which will be blurred.
    :param ori_y: int, the y coordinate which indicate the location of pixel which will be blurred.
    """
    x = ori_x - 1
    y = ori_y - 1
    total_red = 0
    total_green = 0
    total_blue = 0
    pixel_count = 0
    for i in range(3):
        for j in range(3):
            if 0 <= x + i < old_img.width and 0 <= y + j < old_img.height:
                pixel_count += 1
                total_red += old_img.get_pixel(x+i, y+j).red
                total_green += old_img.get_pixel(x+i, y+j).green
                total_blue += old_img.get_pixel(x+i, y+j).blue
    new_img_pixel = new_img.get_pixel(ori_x, ori_y)
    new_img_pixel.red = total_red // pixel_count
    new_img_pixel.green = total_green // pixel_count
    new_img_pixel.blue = total_blue // pixel_count


def main():
    """
    get a picture and blur it for many times.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(9):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
