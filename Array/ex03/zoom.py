import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    try:
        img = ft_load("animal.jpeg")

        if img.ndim != 3:
            raise AssertionError("Image must have 3 dimensions (H, W, C).")

        height, width, channels = img.shape
        if height < 400 or width < 400:
            raise AssertionError("Image is too small for a 400x400 zoom.")

        half = 200
        cy = height // 2
        cx = width // 2

        y_start = cy - half
        y_end = cy + half
        x_start = cx - half
        x_end = cx + half

        zoom = img[y_start:y_end, x_start:x_end, 0:1]

        print("New shape after slicing:", zoom.shape)
        print(zoom)
        zoom_2d = zoom[:, :, 0]
        plt.imshow(zoom_2d, origin="upper")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.title("Zoomed image")
        plt.show()

    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
