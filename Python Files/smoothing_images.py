import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread(r"C:\Users\hi\Downloads\opencv-4.x\samples\data\lena.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel =np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))  # untill above for homogeneous filter
gblur=cv2.GaussianBlur(img,(5,5),0) #for gaussian filter
median=cv2.medianBlur(img,5) #for median filter
bilateralFilter=cv2.bilateralFilter(img,9,75,75) #bilateral filter


titles=["Image","2D convolution","Blur","GBlur","Median","Bilateral Filter"]
images=[img,dst,blur,gblur,median,bilateralFilter]

for i in range(6):
    plt.subplot(3,4,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
