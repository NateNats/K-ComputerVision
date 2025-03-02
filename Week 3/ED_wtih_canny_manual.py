import cv2
import numpy as np

def gaussian_blur(image):
    """Gunakan GaussianBlur bawaan OpenCV"""
    return cv2.GaussianBlur(image, (5, 5), 1.4)

def sobel_gradient(image):
    """Hitung gradien menggunakan Sobel"""
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    direction = np.arctan2(grad_y, grad_x)
     
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    return magnitude, direction

def non_maximum_suppression(magnitude, direction):
    """Menekan piksel yang bukan bagian dari edge utama"""
    M, N = magnitude.shape
    suppressed = np.zeros((M, N), dtype=np.uint8)
    angle = np.rad2deg(direction) % 180
    
    for i in range(1, M-1):
        for j in range(1, N-1):
            q, r = 0, 0  # Perbaikan nilai default
             
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q, r = magnitude[i, j+1], magnitude[i, j-1]
            elif (22.5 <= angle[i, j] < 67.5):
                q, r = magnitude[i-1, j+1], magnitude[i+1, j-1]
            elif (67.5 <= angle[i, j] < 112.5):
                q, r = magnitude[i-1, j], magnitude[i+1, j]
            elif (112.5 <= angle[i, j] < 157.5):
                q, r = magnitude[i-1, j-1], magnitude[i+1, j+1]
             
            if magnitude[i, j] >= q and magnitude[i, j] >= r:
                suppressed[i, j] = magnitude[i, j]
            else:
                suppressed[i, j] = 0
                
    return suppressed

def double_threshold(image, low, high):
    """Gunakan threshold ganda"""
    strong = 255
    weak = 75
    
    strong_i, strong_j = np.where(image >= high)
    weak_i, weak_j = np.where((image <= high) & (image >= low))
    
    thresholded = np.zeros_like(image, dtype=np.uint8)
    thresholded[strong_i, strong_j] = strong
    thresholded[weak_i, weak_j] = weak
    
    return thresholded, weak, strong

def edge_tracking_by_hysteresis(image, weak, strong=255):
    """Pelacakan edge dengan hysteresis"""
    M, N = image.shape
    for i in range(1, M-1):
        for j in range(1, N-1):
            if image[i, j] == weak:
                if ((image[i+1, j-1] == strong) or (image[i+1, j] == strong) or (image[i+1, j+1] == strong)
                    or (image[i, j-1] == strong) or (image[i, j+1] == strong)
                    or (image[i-1, j-1] == strong) or (image[i-1, j] == strong) or (image[i-1, j+1] == strong)):
                    image[i, j] = strong
                else:
                    image[i, j] = 0
    return image

def manual_canny(image_path, width=600, height=400, low_threshold=10, high_threshold=50):
    """Deteksi tepi menggunakan metode Canny secara manual"""
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Gambar tidak ditemukan atau tidak bisa dibaca.")
        return
    
    image_resized = cv2.resize(image, (width, height))
    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    
    # 1. Gaussian Blur
    blurred = gaussian_blur(gray)
    
    # 2. Gradien dengan Sobel
    magnitude, direction = sobel_gradient(blurred) 
    print("Magnitude Min-Max:", np.min(magnitude), np.max(magnitude))
    
    # 3. Non-Maximum Suppression
    suppressed = non_maximum_suppression(magnitude, direction) 
    print("Suppressed Min-Max:", np.min(suppressed), np.max(suppressed))
    
    # 4. Double Threshold
    thresholded, weak, strong = double_threshold(suppressed, low_threshold, high_threshold)
    
    # 5. Edge Tracking by Hysteresis
    final_edges = edge_tracking_by_hysteresis(thresholded, weak, strong)
     
    edges_bgr = cv2.cvtColor(final_edges, cv2.COLOR_GRAY2BGR)
     
    combined = np.hstack((image_resized, edges_bgr))

    # Menampilkan hasil
    cv2.imshow('Original | Manual Canny Edge Detection', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
image_path = r"C:\Users\LEGION\OneDrive\Documents\1. kuliah\komputer vision\K-ComputerVision\Week 3\dataset\gambar4.jpg"
manual_canny(image_path, width=600, height=600, low_threshold=10, high_threshold=50)
