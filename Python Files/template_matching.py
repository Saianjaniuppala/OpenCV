import numpy as np
import cv2 as cv

img=cv.imread(r'C:\Users\hi\Downloads\opencv-4.x\samples\data\messi5.jpg')
grey_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
template=cv.imread(r'C:\Users\hi\Downloads\opencv-4.x\samples\data\messi_face.png',0)
w,h=template.shape[::-1]

res=cv.matchTemplate(grey_img,template,cv.TM_CCORR_NORMED)
print(res)
threshold=0.9;
loc=np.where(res>=threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+ w, pt[1]+h), (0, 0, 255), 2)

cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()