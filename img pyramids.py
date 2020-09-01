'''
import cv2
import numpy as np

img=cv2.imread('lena.jpg')
lr=cv2.pyrDown(img)
lr1=cv2.pyrDown(lr)
# lu=cv2.pyrUp(img)
lu1=cv2.pyrUp(lr1)

cv2.imshow('original img', img)
cv2.imshow('down img', lr)
cv2.imshow('down1 img', lr1)
# cv2.imshow('up img', lu)
cv2.imshow('up1 img', lu1)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2
import numpy as np

img=cv2.imread('lena.jpg')
layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

lp=[layer]
for j in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp[j])
    laplacian =cv2.subtract(gp[j-1], gaussian_extended)
    cv2.imshow(str(j), laplacian)

cv2.imshow('original img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()