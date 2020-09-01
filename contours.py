import cv2
import numpy as np

img=cv2.imread('opencv-logo-white.png')
img1=cv2.imread('opencv-logo-white.png',0)
ret, thresh = cv2.threshold(img1,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Number of contours= '+str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, 11, (1,255,0), 3)

cv2.imshow('original', img)
cv2.imshow('original1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()