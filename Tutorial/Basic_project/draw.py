import cv2
import numpy as np

image = np.zeros([300, 300, 3],dtype=np.uint8)

#cv2.line(image, starting victor, ending victor, colour, thickness)
cv2.line(image, (100,200), (250,250), (250,0,0), 2)

#cv2.rectangle(image, first victor, opposite point victor, colour, thickness of lines)
cv2.rectangle(image, (30,100), (60,150),  (0,255,0), 2)

#cv2.circle(image, center of the circle, radius, color, thickness of the ring)
cv2.circle(image, (150,100), 20, (0,0,250), 3)

#You can type and draw text with it
cv2.putText(image, "hello", (100, 50), 0, 1, (255,255,255), 2 ,1)

cv2.imshow("image",image)
cv2.waitKey()