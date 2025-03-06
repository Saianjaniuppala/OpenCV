OpenCV Projects README

Overview

This README provides an overview of the OpenCV-based projects and scripts that have been executed. The scripts cover various computer vision techniques, including face detection, image blending, shape detection, background subtraction, and feature detection.

Installation

To run these OpenCV scripts, ensure that you have OpenCV and necessary dependencies installed.

Install OpenCV and Contrib Modules

pip install opencv-python opencv-contrib-python numpy

Scripts and Their Functionalities

1. Face Detection (Image & Video)

Uses Haar Cascades to detect faces in images and videos.

Draws bounding boxes around detected faces.

Common Issues & Fixes:

Ensure the correct path to the Haar cascade file.

Verify that the image or video file exists and is readable.

2. Image Blending

Uses image pyramids to blend two images seamlessly.

Employs Laplacian and Gaussian pyramids for smooth transitions.

Common Issues & Fixes:

Ensure both images have the same dimensions.

Verify that OpenCV is correctly installed.

3. Shape Detection

Converts an image to grayscale and applies contour detection.

Identifies and labels different geometric shapes.

Common Issues & Fixes:

Ensure the image path is correct.

Verify that shapes.jpg is available in the specified location.

4. Harris Corner Detection

Applies the Harris Corner Detector to an image.

Marks detected corners in red.

Common Issues & Fixes:

Ensure the input image exists.

Use cv2.imshow() only after verifying the image is loaded.

5. Background Subtraction (MOG & MOG2)

Uses cv.createBackgroundSubtractorMOG2() to detect moving objects in a video.

Displays the original frame and the foreground mask.

Common Issues & Fixes:

If cv.bgsegm.createBackgroundSubtractorMOG() raises an error, install opencv-contrib-python.

Ensure the video file path is correct.

How to Run

For image processing scripts:

python script_name.py

For video-based scripts:

python script_name.py
Press 'q' to exit

Troubleshooting

Image not loading? Check the file path and ensure the file exists.

AttributeError in OpenCV? Install the correct version of OpenCV using:

pip install --upgrade opencv-python opencv-contrib-python

Video not playing? Ensure the file path is correct and try using a different video format.

Future Enhancements

Add real-time face detection with deep learning-based models.

Improve background subtraction using advanced segmentation techniques.

Implement edge detection with Canny and Sobel filters.

Contact

For any issues, feel free to reach out!

