import cv2
import numpy as np

def detect_edges(image_path, width=600, height=400):
    # Membaca gambar
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Gambar tidak ditemukan atau tidak bisa dibaca.")
        return
    
    # Resize gambar agar sesuai ukuran yang diinginkan
    image_resized = cv2.resize(image, (width, height))

    # Konversi ke grayscale
    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

    # Menggunakan algoritma Canny untuk deteksi tepi
    edges = cv2.Canny(gray, 150, 200)

    # Ubah hasil Canny ke format BGR agar bisa digabung dengan gambar asli
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Gabungkan gambar asli dan hasil deteksi tepi dalam satu tampilan
    combined = np.hstack((image_resized, edges_bgr))

    # Menampilkan hasil
    cv2.imshow('Original | Edge Detection', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Contoh penggunaan
image_path = r"C:\Users\LEGION\OneDrive\Documents\1. kuliah\komputer vision\K-ComputerVision\Week 3\dataset\gambar4.jpg"
detect_edges(image_path, width=600, height=600)  # Sesuaikan ukuran sesuai kebutuhan
