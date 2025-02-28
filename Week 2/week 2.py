import cv2
import customfunc as cf
import matplotlib.pyplot as plt

# read image
img = cv2.imread('image.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# scaling
scaled_img = cf.scaling(img, 0.5, 0.5)

# rotation
rotated_img = cf.rotate(img, 180)

# translation
cf.debug_img(rotated_img, "scaled image", (12, 8), True)