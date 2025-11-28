import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array):
    """
    Inverts the color values of `array`.
    """
    image = 255 - array
    plt.imshow(image)
    plt.show()


def ft_red(array):
    """
    Keeps only the red channel.
    """
    image = array * np.array([1, 0, 0])
    plt.imshow(image)
    plt.show()


def ft_green(array):
    """
    Keeps only the green channel.
    """
    image = array.copy()
    image[..., 0] = image[..., 0] - image[..., 0]
    image[..., 2] = image[..., 2] - image[..., 2]
    plt.imshow(image)
    plt.show()


def ft_blue(array):
    """
    Keeps only the blue channel.
    """
    image = array.copy()
    image[..., 0] = 0
    image[..., 1] = 0
    plt.imshow(image)
    plt.show()


def ft_grey(array):
    """
    Converts image to grayscale.
    """
    grey = array.copy()
    grey_channel = array[..., 0] / 3
    grey[..., 0] = grey_channel
    grey[..., 1] = grey_channel
    grey[..., 2] = grey_channel
    plt.imshow(grey)
    plt.show()
