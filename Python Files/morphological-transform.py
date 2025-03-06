import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\hi\Downloads\opencv-4.x\samples\data\smarties.png", cv2.IMREAD_GRAYSCALE)


if img is None:
    print("Error: Image not loaded. Check the file path.")
    exit()
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)


kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1) 
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)

titles = ["Image", "Mask", "Dilation", "Erosion","Opening","Closing","Gradient","Tophat"]
images = [img, mask, dilation, erosion,opening,closing,mg,th]

for i in range(8):  
    plt.subplot(4, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()  
