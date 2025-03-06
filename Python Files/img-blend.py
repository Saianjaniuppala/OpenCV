import cv2
import numpy as np

# Load images
apple = cv2.imread(r"C:\Users\hi\Downloads\opencv-4.x\samples\data\apple.jpg")
orange = cv2.imread(r"C:\Users\hi\Downloads\opencv-4.x\samples\data\orange.jpg")

print(apple.shape)
print(orange.shape)

# Simple half-and-half blending
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# Generate Gaussian pyramids
gp_apple = [apple.copy()]
gp_orange = [orange.copy()]
for i in range(6):
    gp_apple.append(cv2.pyrDown(gp_apple[-1]))
    gp_orange.append(cv2.pyrDown(gp_orange[-1]))

# Generate Laplacian pyramids
lp_apple = [gp_apple[-1]]
lp_orange = [gp_orange[-1]]

for i in range(5, 0, -1):
    lp_apple.append(cv2.subtract(gp_apple[i - 1], cv2.pyrUp(gp_apple[i])))
    lp_orange.append(cv2.subtract(gp_orange[i - 1], cv2.pyrUp(gp_orange[i])))

# Merge pyramids
apple_orange_pyramid = []
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols / 2)], orange_lap[:, int(cols / 2):]))  # Fixed line
    apple_orange_pyramid.append(laplacian)

# Reconstruct the blended image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)

    # Resize the upsampled image to match the pyramid level
    apple_orange_reconstruct = cv2.resize(apple_orange_reconstruct, (apple_orange_pyramid[i].shape[1], apple_orange_pyramid[i].shape[0]))

    # Now add both images
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

# Display images
cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
cv2.imshow("Blended Image", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
