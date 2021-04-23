"""
File: blur.py
Name: DiCheng
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Using pixel coordinates to get the pixel and its neighbors for average of rgb and then get blurred.
    :param img: SimpleImage, the image object which will be blurred.
    :return: SimpleImage, the image which were all blurred.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(new_img.width):
        for y in range(new_img.height):
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            neighbor_pixels_num = 0
            new_img_p = new_img.get_pixel(x, y)
            for i in range(3):
                for j in range(3):
                    if 0 <= x + (i-1) < img.width and 0 <= y + (j-1) < img.height:
                        neighbor_pixels_num += 1
                        sum_red += img.get_pixel(x + (i-1), y + (j-1)).red
                        sum_green += img.get_pixel(x + (i-1), y + (j-1)).green
                        sum_blue += img.get_pixel(x + (i-1), y + (j-1)).blue
            new_img_p.red = sum_red // neighbor_pixels_num
            new_img_p.green = sum_green // neighbor_pixels_num
            new_img_p.blue = sum_blue // neighbor_pixels_num
    return new_img


def main():
    """
    get a picture and blur it for given times.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
    main()
