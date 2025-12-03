from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """
    Load a JPEG image from `path` into a NumPy array and print its shape.
    """
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Wrong format")
    except AssertionError as e:
        print("AssertionError:", e)
        return None

    try:
        img = Image.open(path)
    except FileNotFoundError:
        print("AssertionError: File not found")
        return None

    arr = np.array(img)
    print("The shape of image is:", arr.shape)
    print(arr)
    return arr


def main():
    pass


if __name__ == "__main__":
    main()
