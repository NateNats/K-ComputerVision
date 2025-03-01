import cv2
import customfunc as cf
import matplotlib.pyplot as plt

# read image
img = cv2.imread('image.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# scaling
# scaled_img = cf.scaling(img, 0.5, 0.5)

# rotation
# rotated_img = cf.rotate(img, 180)

# translation
# translated_img = cf.translation(img, 50, 150)
# translated_img.show()

# skewing
skewed_img = cf.skewing(img, 0.3, 0.3)
skewed_img.show()

# cf.debug_img(rotated_img, "translated image", (12, 8), True)