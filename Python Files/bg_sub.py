import cv2 as cv
import numpy as np
cap=cv.VideoCapture(r'C:\Users\hi\Downloads\opencv-4.x\samples\data\vtest.avi')

fgbg=cv.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    ret,frame=cap.read()
    if frame is None:
        break
    fgmask=fgbg.apply(frame)


    cv.imshow("Frame",frame)
    cv.imshow("FG Mask Frame",fgmask)

    keyboard=cv.waitKey(30)
    if keyboard=='q' or keyboard==27:
        break

cap.release()
cv.destroyAllWindows()