import cv2
import matplotlib.pyplot as plt
import numpy as np
import functionality

if __name__ == "__main__":
    fun = functionality.PyImageSearchANPR(4, 5, True)
    fun.license_plate_candidate('dataset/img.jpeg')