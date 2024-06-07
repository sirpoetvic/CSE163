import imageio
from matplotlib.animation import adjusted_figsize
import matplotlib.pyplot as plt
import numpy as np


def blur_image(file_in, file_out, kernel_size):
    """
    file_in is the name of the file to blur
    file_out is the name of the output file
    kernel_size is >= 3 and is the size of the kernel used to blur
    The method will create a blurred image of the original by
    applying a blur kernel (a convolution). The kernel will be
    applied to each of the 3 color channels. It is a 2D matrix
    of all 1's and averaged by the number of elements. For example,
    a 3x3 kernel will average the 9 elements' values.
    """
    image = imageio.imread(file_in)
    num_rows, num_col, _ = image.shape

    # prep the image
    blurred_image = np.zeros_like(image)

    adjusted = image * (1 / (kernel_size**2))

    # check through the rows? by the length of the kernel
    # iterate through rows
    for row in range(num_rows - kernel_size):
        for col in range(num_col - kernel_size):
            for color in range(3):
                local_total = np.sum(
                    adjusted[
                        row : row + kernel_size,
                        col : col + kernel_size,
                        color,
                    ]
                )
                blurred_image[
                    row + int(kernel_size / 2),
                    col + int(kernel_size / 2),
                    color,
                ] = local_total
    imageio.imwrite(file_out, blurred_image)


def edge_detect(file_in, file_out, channel):
    """
    file_in is the name of the file to detect edges
    file_out is the name of the output file, in gray scale only.
    Channel is: 0=Red, 1=Green, 2=Blue
    """
    # The input file will have 3 color channels. Instead of averaging
    # the 3 colors (RGB), use only a single channel as the input.
    # Use the edge detection kernel of size 3x3.
    # If the resulting value <=127 then make it 0, else 255.
    image = imageio.imread(file_in)
    channel_only = image[:, :, channel]
    adjusted_image = np.zeros_like(channel_only)
    kernel = [
        [
            -1,
            -1,
            -1,
        ],
        [-1, 8, -1],
        [
            -1,
            -1,
            -1,
        ],
    ]

    num_rows, num_col, _ = image.shape

    for row in range(1, num_rows - 1):
        for col in range(1, num_col - 1):
            region = channel_only[row - 1 : row + 2, col - 1 : col + 2]
            num = np.sum(region * kernel)
            adjusted_image[row, col] = 255 if num >= 127 else 0
    imageio.imwrite(file_out, adjusted_image)


def duckie_hat():
    """
    Add a green hat to the duck as described in the online lessons.
    The main-hat should be a rectangle with the top-left corner at (20, 85)
    and the bottom-right corner at (75, 135).
    The hat brim should be a rectangle with the top-left corner at (75, 60)
    and the bottom-right corner at (90, 160).
    """

    # Read in the image
    duck = imageio.imread("duck.jpg")

    duck_copy = duck.copy()

    # Main hat is a green rectangle with top-left
    # at (20,85) bottom-right corner at (75, 135)
    duck_copy[20:75, 85:135, 0] = 0
    duck_copy[20:75, 85:135, 1] = 255
    duck_copy[20:75, 85:135, 2] = 0

    # Main hat is a green rectangle with top-left
    # at (75,60) bottom-right corner at (90, 160)
    duck_copy[75:90, 60:160, 0] = 0
    duck_copy[75:90, 60:160, 1] = 255
    duck_copy[75:90, 60:160, 2] = 0

    return duck_copy


def main():
    duckie_hat()
    edge_detect("duck.jpg", "edge.jpg", 0)
    blur_image("duck.jpg", "blur.jpg", 5)


if __name__ == "__main__":
    main()
