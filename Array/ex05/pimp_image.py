#import matplotlib.pyplot as plt
#from load_image import ft_load


def ft_invert(array):
    """
    Invert the color values of `array`
    (255 - array) and print the result.
    """
    image = 255 - array
    print(image)
    return image
