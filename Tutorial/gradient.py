import cv2

gray = cv2.imread("/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/photos/opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

#Second order derivative, used to find edges in an image
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

#Canny edge detector, if the pixel stage is bigger than 200, then it's considered as an edge, better than laplacian
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("gray",gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)

cv2.waitKey()
