import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread(r'C:\Users\hi\Downloads\opencv-4.x\samples\data\lena.jpg')
#img=np.zeros((200,200),np.uint8)
#cv.rectangle(img,(0,100),(200,200),255,-1)
#cv.rectangle(img,(0,50),(100,100),127,-1)
#b,q,r=cv.split(img)

hist=cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)

# cv.imshow("Image",img)
# cv.imshow("b",b)
# cv.imshow("q",q)
# cv.imshow("r",r)
# plt.hist(b.ravel(),256,[0,256])
# plt.hist(q.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()