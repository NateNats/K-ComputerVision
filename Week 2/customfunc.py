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

# rotation function
def rotation(img, angle):
    frame = Image.fromarray(img)
    width, height = frame.size
    theta = math.radians(angle)
    

    pass