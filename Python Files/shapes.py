import cv2

image_path = r"C:\Users\hi\Downloads\opencv-4.x\samples\data\lena.jpg"  # Use raw string
img = cv2.imread(image_path)
img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),7)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)

if img is None:
    print("Error: Image not found or can't be read!")
else:
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
