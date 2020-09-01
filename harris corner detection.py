import cv2
import numpy as np

img=cv2.imread('blox.jpg')
gray=cv2.imread('blox.jpg',0)

gray=np.float32(gray)
dst=cv2.cornerHarris(gray, 2,3,0.04)

dst=cv2.dilate(dst, None)

img[dst>0.01 * dst.max()]=[0,0,255]

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()