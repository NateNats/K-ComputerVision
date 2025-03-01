import matplotlib.pyplot as plt
from PIL import Image
import math
import numpy as np

# scaling function
def scaling(image, scale_x=1.0, scale_y=1.0, target_size=None):
    img = Image.fromarray(image)

    if target_size:
        scaled_img = img.resize(target_size)
    else:
        new_width, new_height = int(img.width * scale_x), int(img.height *  scale_y)
        scaled_img = img.resize((new_width, new_height))
    return scaled_img

# grayscale
def grayscale(image):
    img  = Image.fromarray(image)
    r = img.getchannel(0)

    width, height = img.size
    grayscale_img = np.zeros((height, width), np.uint8)

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            gray_val = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            grayscale_img[y][x] = gray_val

    return Image.fromarray(grayscale_img)


def debug_img(img, title=None, figure_size=(12, 8), waitkey=False):
    plt.figure(figsize=figure_size)
    plt.title(title)
    plt.imshow(img)
    if waitkey:
        plt.waitforbuttonpress()


# translation
def translation(image, tx, ty):
    img = Image.fromarray(image)
    width, height = img.size
    translated_img = Image.new("RGB", (width, height), (0, 0, 0))

    for x in range(width):
        for y in range(height):
            new_x = x + tx
            new_y = y + ty

            if 0 <= new_x < width and 0 <= new_y < height:
                translated_img.putpixel((new_x, new_y), img.getpixel((x, y)))

    return translated_img


# skewing
def skewing(image, sx, sy):
    img = Image.fromarray(image)
    width, height = img.size
    skewed_img = Image.new("RGB", (width, height))
    new_width, new_height = int(width * abs(sx)), int(height * abs(sy))

    for x in range(width):
        for y in range(height):
            new_x = int(x + sx * (y - height // 2) + new_width // 2)
            new_y= int(y + sy * (x - width // 2) + new_height // 2)

            if 0 <= new_x < width and 0 <= new_y < height:
                skewed_img.putpixel((new_x, new_y), img.getpixel((x, y)))

    return skewed_img


# rotation function
def rotate(image, angle):
    img = Image.fromarray(image)
    width, height = img.size
    theta = math.radians(angle)
    sin = math.sin(theta)
    cos = math.cos(theta)

    #   [ X^         [Cos theta     -Sin theta  ]   [ x - xc
    #           =
    #   y^ ]         [Sin theta       Cos theta ]    y  - yc ]
    new_width = int(abs(width * cos) + abs(height * sin))
    new_height = int(abs(width * sin) + abs(height * cos))
    rotated_img = Image.new('RGB', (new_width, new_height), (0, 0, 0))
    xc, yc = (width // 2), (height // 2)
    new_xc, new_yc = (new_width // 2), (new_height // 2)

    for x in range(width):
        for y in range(height):
            x_shifted = x - xc
            y_shifted = y - yc
            new_x = int(x_shifted * cos - y_shifted * sin + new_xc)
            new_y = int(x_shifted * sin + y_shifted * cos + new_yc)

            if 0 <= new_x < width and 0 <= new_y < height:
                rotated_img.putpixel((new_x, new_y), img.getpixel((x, y)))

    return rotated_img


def thresholding(image, threshold=128):
    img = Image.fromarray(image)

    if img.mode == "RGB":
        img = img.convert("L")

    width, height = img.size
    binary_img = np.zeros((height, width), dtype=np.uint8)

    for x in range(width):
        for y in range(height):
            if img.getpixel((x, y)) > threshold:
                binary_img[y, x] = 255
            else:
                binary_img[y, x] = 0

    return Image.fromarray(binary_img)


def noise_reduction(image, kernel_size=3, filter="mean"):
    img = Image.fromarray(image)

    if img.mode == "RGB":
        img = img.convert("L")

    img_array = np.array(img)
    height, width = img_array.shape
    pad = kernel_size // 2
    filtered_img = np.zeros((height, width), dtype=np.uint8)
    padded_img = np.pad(img_array, pad, mode="constant", constant_values=0)

    for i in range(height):
        for j in range(width):
            region = padded_img[i:i + kernel_size, j:j + kernel_size]
            if filter == "mean":
                filtered_img[i, j] = np.mean(region)
            elif filter == "median":
                filtered_img[i, j] = np.median(region)

    return Image.fromarray(filtered_img)