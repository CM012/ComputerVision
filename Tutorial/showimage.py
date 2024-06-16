import cv2
image=cv2.imread("Tutorial/photos/opencv_logo.jpg")
print(image.shape)
cv2.imshow("image",image)
cv2.waitKey()