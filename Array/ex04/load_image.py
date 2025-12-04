import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load a JPEG image from `path` into a NumPy array and print its shape.
    """
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Wrong format")
    except AssertionError as error:
        print("AssertionError: ", error)
        return []
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print("FileNotFoundError: Cant find img")
        return []
    except Exception as error:
        print("Error: An unexpected error occurred:", error)
        return []
    arr = np.array(img)
    print("The shape of image is:", arr.shape)
    print(arr)
    return arr
