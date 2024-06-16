import cv2

#That means you only read the greyscale of the photo
gray = cv2.imread("/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/photos/bookpage.jpg", cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#Cut the photo into six parts and handle them individually
binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#common way of threshold, you don't need to determine the threshold yourself, it's calculated automatically
#not that useful in this case, but useful in most of the cases since you don't need to determine
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("adaptive", binary_adaptive)
cv2.imshow("otsu", binary_otsu)

cv2.waitKey()

