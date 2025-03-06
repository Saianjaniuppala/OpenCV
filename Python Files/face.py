import cv2 as cv
import os

image_path = r"C:\Users\hi\Downloads\opencv-4.x\samples\data\test.png"

# Check if the file exists before loading
if not os.path.exists(image_path):
    print("Error: Image file not found!")
    exit()

img = cv.imread(image_path)

if img is None:
    print("Error: Image could not be read!")
    exit()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier(r'C:\Users\hi\Downloads\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv.imshow("Face Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()
