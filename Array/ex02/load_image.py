import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load a JPEG image from `path` into a NumPy array and print its shape.
    """
    assert path.lower().endswith(
        (".jpg", ".jpeg", ".JPG", ".JPEG")
    ), "Wrong format"
    try:
        img = Image.open(path)
    except FileNotFoundError as err:
        raise AssertionError("File not found") from err

    arr = np.array(img)
    print("The shape of image is:", arr.shape)
    print(arr)
    return arr
