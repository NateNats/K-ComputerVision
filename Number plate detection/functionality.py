import matplotlib.pyplot as plt
from skimage.segmentation import clear_border
import pytesseract
import numpy as np
import imutils
import cv2

class PyImageSearchANPR:
    def __init__(self, minAR = 4, maxAR = 5, debug=False):
        # eropa dan plat nomer internasinal memiliki ukuran plat lebih panjang daripada
        # milik US yang lebih tinggi daripada internasional, dan plat nomer indonesia lebih
        # tinggi

        self.minAR = minAR
        self.maxAR = maxAR
        self.debug = debug

    def debug_imshow(self, title, image, waitKey=False):
        if self.debug:
            plt.title(title)
            plt.imshow(image)

            if waitKey:
                plt.waitforbuttonpress()

    def license_plate_candidate(self, image, keep=5):
        # convert an image to binary
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
        _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        reckern = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
        blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel=reckern)
        self.debug_imshow("dark region", blackhat, waitKey=True)


        # ada 2 model, pertama buat deteksi motor, terus model satu lagi buat deteksi plat