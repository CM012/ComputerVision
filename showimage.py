import cv2
image=cv2.imread("/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/opencv_logo.jpg")
print(image.shape)
cv2.imshow("image",image)
cv2.waitKey()