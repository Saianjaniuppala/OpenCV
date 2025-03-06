import cv2
import numpy as np

img = cv2.imread(r"C:\Users\hi\Downloads\opencv-4.x\samples\data\lena.jpg")
layer=img.copy()
gp=[layer]
#lr1=cv2.pyrDown(img)
#lr2=cv2.pyrDown(lr1)
#hr=cv2.pyrUp(lr2)

for i in range(6):
    layer=cv2.pyrDown(layer) # layers in laplacian pyramids
    gp.append(layer)
    cv2.imshow(str(i),layer)

cv2.imshow("Original Image",img)# normal in gaussian pyramids
#cv2.imshow("PyrDown 1 img",lr1)
#cv2.imshow("PyrDown 2 img",lr2)
#cv2.imshow("PyrUp img",hr)

cv2.waitKey(0)
cv2.destroyAllWindows()