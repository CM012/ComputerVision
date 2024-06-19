import cv2
import numpy as np

gray = cv2.imread("/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/Basic_project/photos/opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

#Reverse white to black
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(binary, kernel)
#Opposite of erosion
dilation = cv2,dilate(binary, kernel, 1)

cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)

cv2.waitKey()