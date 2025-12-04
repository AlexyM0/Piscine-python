import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        img = ft_load("animal.jpeg")

        if img is None or img.ndim != 3:
            return

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
        zoom_2d = zoom[:, :, 0]
        h, w = zoom_2d.shape
        print(f"New shape after slicing: {zoom.shape} or ({h}, {w})")
        print(zoom)
        plt.imshow(zoom_2d, cmap='gray', origin="upper")
        plt.show()

    except AssertionError as e:
        print("AssertionError: ", e)


if __name__ == "__main__":
    main()
