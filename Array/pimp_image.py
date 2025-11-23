import matplotlib.pyplot as plt
from load_image import ft_load

def ft_invert(array) -> array:
    image = 255 - array
    print(image)
    return image

