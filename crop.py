import cv2

image=cv2.imread("/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/opencv_logo.jpg")

#crop[row(range), column(range)]
crop = image[10:170,40:200]

cv2.imshow("crop", crop)
cv2.waitKey()