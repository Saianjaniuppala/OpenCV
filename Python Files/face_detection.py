import cv2 as cv

face_cascade=cv.CascadeClassifier(r'C:\Users\hi\Downloads\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade=cv.CascadeClassifier(r'C:\Users\hi\Downloads\opencv-4.x\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml')

#img=cv.imread(r'C:\Users\hi\Downloads\opencv-4.x\samples\data\test.png')
cap = cv.VideoCapture(r'C:\Users\hi\Downloads\opencv-4.x\samples\data\test.mp4')

while cap.isOpened():
    _, img=cap.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)
    cv.imshow("img",img)
    if cv.waitKey(30) & 0xFF==ord('q'):
        break

cap.release()
# cv.waitKey()
# cv.destroyAllWindows()