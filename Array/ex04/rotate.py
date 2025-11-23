import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    try:
        img = ft_load("animal.jpeg")

        if img.ndim != 3:
            raise AssertionError("Image must have 3 dimensions (H, W, C).")

        height, width, _ = img.shape
        if height < 400 or width < 400:
            raise AssertionError("Image is too small for a 400x400 crop.")

        half = 200
        cy = height // 2
        cx = width // 2

        y_start = cy - half
        y_end = cy + half
        x_start = cx - half
        x_end = cx + half

        square = img[y_start:y_end, x_start:x_end, :]
        gray = square[:, :, 0:1]

        h, w, c = gray.shape
        print(f"The shape of image is: ({h}, {w}, {c}) or ({h}, {w})")
        print(gray)

        gray_2d = gray[:, :, 0]
        rotated = gray_2d.T

        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)

        plt.imshow(rotated, origin="upper", cmap="gray")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.title("Transposed square image")
        plt.show()

    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
