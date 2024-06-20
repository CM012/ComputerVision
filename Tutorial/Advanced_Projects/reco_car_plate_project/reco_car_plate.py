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

def sort_countours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key = lambda b: b[1][i], reverse=reverse))

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
print(np.array(refCnts).shape)

#To order the frames
refCnts= myutils.sort_countours(refCnts, method="left-to-right")[0]
digits={}

# Every figure
for (i, c) in enumerate(refCnts):
    #resize the bounding box to the optimal size
    (x, y, w, h) = cv2.boundingRect(c)
    roi = ref[y:y + h, x:x + w]
    roi = cv2.resize(roi, (57, 88))

    #Every digit to each template
    digits[i] = roi

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
sqlKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

image = cv2.imread(args["/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/Advanced_Projects/reco_car_plate_project/Materials/credit_card.jpg"])
