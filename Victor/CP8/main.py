import imageio
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
    pass


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
    pass


def duckie_hat():
    """
    Add a green hat to the duck as described in the online lessons.
    The main-hat should be a rectangle with the top-left corner at (20, 85)
    and the bottom-right corner at (75, 135).
    The hat brim should be a rectangle with the top-left corner at (75, 60)
    and the bottom-right corner at (90, 160).
    """
    pass


def main():
    duckie_hat()
    edge_detect("duck.jpg", "edge.jpg", 0)
    blur_image("duck.jpg", "blur.jpg", 5)


if __name__ == "__main__":
    main()
