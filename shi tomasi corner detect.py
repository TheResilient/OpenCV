import cv2
import numpy as np

img=cv2.imread('pic1.png')
gray=cv2.imread('pic1.png',0)

gray=np.float32(gray)
dst=cv2.goodFeaturesToTrack(gray, 25,0.01,10)

dst=np.int0(dst)

for i in dst:
    x,y=i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()