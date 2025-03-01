import matplotlib.pyplot as plt
from PIL import Image
import math

# scaling function
def scaling(image, scale_x=1.0, scale_y=1.0, target_size=None):
    img = Image.fromarray(image)

    if target_size:
        scaled_img = img.resize(target_size)
    else:
        new_width, new_height = int(img.width * scale_x), int(img.height *  scale_y)
        scaled_img = img.resize((new_width, new_height))
    return scaled_img

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