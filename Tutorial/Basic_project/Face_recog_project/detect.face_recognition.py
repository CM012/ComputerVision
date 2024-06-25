import cv2 as cv

img = cv.imread(
    '/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/Basic_project/photos/group 1.jpg')
cv.imshow('Group of 5 people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier(
    '/Users/charles/Documents/MyProjects/ComputerVision/Tutorial/Basic_project/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale( gray, scaleFactor=1.03, minNeighbors=1, flags= 0, minSize= [20, 20])
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)



cv.waitKey(0)