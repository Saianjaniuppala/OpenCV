import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\hi\Downloads\opencv-4.x\samples\data\messi5.jpg", cv2.IMREAD_GRAYSCALE)
canny=cv2.Canny(img,100,200)
titles=["Images","Canny"]
images=[img,canny]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()