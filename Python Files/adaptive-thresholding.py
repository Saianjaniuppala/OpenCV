import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\hi\Downloads\opencv-4.x\samples\data\sudoku.png', cv.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not loaded. Check the file path.")
    exit()
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("Original Image", img)
cv.imshow("Global Threshold", th1)
cv.imshow("Adaptive Threshold", th2)

cv.waitKey(0)
cv.destroyAllWindows()
