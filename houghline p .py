import cv2 as cv
import numpy as np

img=cv.imread('road.jpg')
gray=cv.imread('road.jpg',0)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('image1', edges)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2,y2= line[0]
    cv.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()