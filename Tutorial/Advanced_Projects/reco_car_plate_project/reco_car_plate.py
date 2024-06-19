from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import myutils

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Get one image
img = cv2.imread(
    "/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/Advanced_Projects/reco_car_plate_project/Materials/template.jpg")
cv_show('img', img)

#Get grey image
ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv_show('ref', ref)

#Get binary image
ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]
cv_show('ref', ref)

#Get the out figure
ref_, refCnts, hierarchy = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, refCnts, -1, (0,0,255), 3)
cv_show('img', img)