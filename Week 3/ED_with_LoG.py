import cv2
import numpy as np

def log_edge_detection(image_path, scale=1.0, ksize=5): 
    # Baca gambar
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Cek jika gambar tidak ditemukan
    if img is None:
        print("Error: Gambar tidak ditemukan! Periksa kembali path gambar.")
        return
    
    # Resize gambar sesuai skala
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

    # Langkah 1: Blur gambar dengan Gaussian untuk mengurangi noise
    img_blur = cv2.GaussianBlur(img, (ksize, ksize), 0)

    # Langkah 2: Terapkan Laplacian untuk deteksi tepi
    laplacian = cv2.Laplacian(img_blur, cv2.CV_64F)

    # Konversi ke format uint8 agar bisa ditampilkan dengan OpenCV
    laplacian = cv2.convertScaleAbs(laplacian)

    # Gabungkan gambar asli, blur, dan hasil Laplacian untuk perbandingan
    combined = np.hstack((img, img_blur, laplacian))

    # Tampilkan hasil
    cv2.imshow("Laplacian of Gaussian (LoG) Edge Detection", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Panggil fungsi dengan path gambar
log_edge_detection(r"C:\Users\LEGION\OneDrive\Documents\1. kuliah\komputer vision\K-ComputerVision\Week 3\dataset\gambar4.jpg", scale=0.4, ksize=3)
