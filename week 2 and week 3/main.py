import cv2
import numpy as np
from customfunc import scaling, grayscale, translation, skewing, rotate, thresholding, noise_reduction, debug_img
from ED_with_canny import manual_canny

# Path gambar
image_path = r"C:\Users\LEGION\OneDrive\Documents\1. kuliah\komputer vision\K-ComputerVision\Week 2 and week 3\dataset\gambar4.jpg"

# Load gambar
image = cv2.imread(image_path)
if image is None:
    print("Error: Gambar tidak ditemukan!")
    exit()

# 1. Skalasi gambar
scaled_image = scaling(image, scale_x=0.5, scale_y=0.5)

# 2. Konversi ke grayscale
gray_image = grayscale(image)

# 3. Translasi gambar
translated_image = translation(image, tx=50, ty=50)

# 4. Skewing gambar
skewed_image = skewing(image, sx=0.2, sy=0.1)

# 5. Rotasi gambar
rotated_image = rotate(image, angle=45)

# 6. Thresholding
thresholded_image = thresholding(image, threshold=128)

# 7. Noise Reduction
denoised_image = noise_reduction(image, kernel_size=3, filter="mean")

# 8. Edge Detection dengan metode manual Canny
manual_canny(image_path, width=600, height=600, low_threshold=10, high_threshold=50)

# Debugging: Menampilkan gambar
debug_img(scaled_image, title="Scaled Image")
debug_img(gray_image, title="Grayscale Image")
debug_img(translated_image, title="Translated Image")
debug_img(skewed_image, title="Skewed Image")
debug_img(rotated_image, title="Rotated Image")
debug_img(thresholded_image, title="Thresholded Image")
debug_img(denoised_image, title="Denoised Image")

# Tampilkan semua hasil
import matplotlib.pyplot as plt
plt.show()
