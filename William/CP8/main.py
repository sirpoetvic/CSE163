import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np


# Write your function here!
def blur_image(file_in, file_out, kernel_size):
    '''
    file_in is the name of the file to blur
    file_out is the name of the output file
    kernel_size is >= 3 and is the size of the kernel used to blur
    The method will create a blurred image of the original by
    applying a blur kernel (a convolution). The kernel will be
    applied to each of the 3 color channels. It is a 2D matrix
    of all 1's and averaged by the number of elements. For example,
    a 3x3 kernel will average the 9 elements' values.
    '''
    duck = imageio.imread(file_in)

    duck_blur = duck.astype(np.float64)

    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)

    half_kernel = kernel_size // 2

    for i in range(duck.shape[0]):
        for j in range(duck.shape[1]):
            # make the region for the current pixel to apply blur later
            i_start = max(0, i - half_kernel)
            i_end = min(duck.shape[0], i + half_kernel + 1)
            j_start = max(0, j - half_kernel)
            j_end = min(duck.shape[1], j + half_kernel + 1)

            # make sure region is of size kernel_size x kernel_size
            region = duck[i_start:i_end, j_start:j_end]

            # make kernel same size as the region it is working on
            kernel_trimmed = kernel[:region.shape[0], :region.shape[1]]

            # apply the kernel to the region for each color channel
            for k in range(duck.shape[2]):
                duck_blur[i, j, k] = np.sum(region[:, :, k] * kernel_trimmed)

    duck_blur /= 255.0

    plt.imshow(duck_blur)
    plt.savefig(file_out)
    # plt.show()


def edge_detect(file_in, file_out, channel):
    '''
    file_in is the name of the file to detect edges
    file_out is the name of the output file, in gray scale only.
    Channel is: 0=Red, 1=Green, 2=Blue
    '''
    duck = imageio.imread(file_in)
    duck_copy = duck.copy()

    # edge detection kernel
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

    edges = np.ones((duck_copy.shape[0], duck_copy.shape[1], 3))

    for i in range(1, duck_copy.shape[0] - 1):
        for j in range(1, duck_copy.shape[1] - 1):
            region = duck_copy[i-1:i+2, j-1:j+2, channel]

            edge_value = np.sum(region * kernel)

            if edge_value <= 127:
                edges[i, j] = 255
            else:
                edges[i, j] = 0

    plt.imshow(edges)
    plt.savefig(file_out)
    # plt.show()


def duckie_hat():
    '''
    Add a green hat to the duck as described in the online lessons.
    The main-hat should be a rectangle with the top-left corner at (20, 85)
    and the bottom-right corner at (75, 135).
    The hat brim should be a rectangle with the top-left corner at (75, 60)
    and the bottom-right corner at (90, 160).
    '''
    duck = imageio.imread("duck.jpg")

    hat_top_left = (20, 85)
    hat_bottom_right = (75, 135)
    brim_top_left = (75, 60)
    brim_bottom_right = (90, 160)

    duck_hat = np.copy(duck)
    # note: [0] = x, [1] = y
    # make the rectangle segment green
    # red
    duck_hat[hat_top_left[0]:hat_bottom_right[0],
             hat_top_left[1]:hat_bottom_right[1], 0] = 0
    # green
    duck_hat[hat_top_left[0]:hat_bottom_right[0],
             hat_top_left[1]:hat_bottom_right[1], 1] = 255
    # blue
    duck_hat[hat_top_left[0]:hat_bottom_right[0],
             hat_top_left[1]:hat_bottom_right[1], 2] = 0

    # make the brim segement green
    # red
    duck_hat[brim_top_left[0]:brim_bottom_right[0],
             brim_top_left[1]:brim_bottom_right[1], 0] = 0
    # green
    duck_hat[brim_top_left[0]:brim_bottom_right[0],
             brim_top_left[1]:brim_bottom_right[1], 1] = 255
    # blue
    duck_hat[brim_top_left[0]:brim_bottom_right[0],
             brim_top_left[1]:brim_bottom_right[1], 2] = 0

    plt.imshow(duck_hat)
    plt.savefig("duckie_hat.png")
    # plt.show()


def main():
    blur_image('duck.jpg', 'blur.jpg', 3)
    edge_detect("duck.jpg", "edge.jpg", 0)
    duckie_hat()


if __name__ == "__main__":
    main()
