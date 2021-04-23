"""
File: best_photoshop_award.py
Name: DiCheng
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""

from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.055

# Controls the upper bound for black pixel
BLACK_PIXEL = 300


def combine_gme(figure_img, stock_img):
    """
    Finding the green pixel of figure image and then replace by stock image pixel.
    :param figure_img: SimpleImage, the image of me.
    :param stock_img: SimpleImage, the image of GME stock run chart.
    :return: SimpleImage, the figure image with green background replaced by stock image.
    """
    stock_img.make_as_big_as(figure_img)
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            figure_pixel = figure_img.get_pixel(x, y)
            avg = (figure_pixel.red+figure_pixel.blue+figure_pixel.green) // 3
            total = figure_pixel.red+figure_pixel.blue+figure_pixel.green
            if figure_pixel.green > avg*THRESHOLD and total > BLACK_PIXEL:
                stock_pixel = stock_img.get_pixel(x, y)
                reassign_rgb_from_pixel(figure_pixel, stock_pixel)
    return figure_img


def combine_cage(figure_img):
    """
    Using the coordinates to build the cage.
    :param figure_img: SimpleImage, the image of me.
    :return: SimpleImage, the image that I'm locked in the stock market.
    """
    cage_row_img = SimpleImage("image_contest/cage_row.jpg")
    cage_column_img = SimpleImage("image_contest/cage_column.jpg")
    # 5 columns
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            for i in range(1, 6, 1):
                if x == figure_img.width // 2 // 3 * i:
                    for cage_x in range(cage_column_img.width):
                        figure_pixel = figure_img.get_pixel(x + cage_x, y)
                        cage_column_pixel = cage_column_img.get_pixel(cage_x, y)
                        reassign_rgb_from_pixel(figure_pixel, cage_column_pixel)
    # 4 rows
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            if y == 0 or y == figure_img.height // 2 // 2 or y == figure_img.height // 2 // 2 * 3 or y == figure_img.height - cage_row_img.height - 1:
                for cage_y in range(cage_row_img.height):
                    figure_pixel = figure_img.get_pixel(x, y + cage_y)
                    cage_row_pixel = cage_row_img.get_pixel(x, cage_y)
                    reassign_rgb_from_pixel(figure_pixel, cage_row_pixel)
    return figure_img


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
    get a figure image and replace the green pixels by stock image, and then build the cage.
    ---
    Design based on true story, BUY AND HOOOOOOOOOOOOOOLLLLLLD~~~
    I just get the ticket for being part of next hollywood movie. :P
    """
    figure_img = SimpleImage("image_contest/figure.JPG")
    figure_img.show()
    stock_img = SimpleImage("image_contest/stock.PNG")
    figure_img = combine_gme(figure_img, stock_img)
    figure_img = combine_cage(figure_img)
    figure_img.show()


if __name__ == '__main__':
    main()
