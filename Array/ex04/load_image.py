from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load a JPEG image from `path` and return it as a NumPy array.
    """
    assert path.lower().endswith(
        (".jpg", ".jpeg", ".JPG", ".JPEG")
    ), "Wrong format"
    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise AssertionError("File not found")

    arr = np.array(img)
    return arr


def main() -> None:
    """
    Placeholder for testing `ft_load`.
    """
    pass


if __name__ == "__main__":
    main()
