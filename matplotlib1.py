'''
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg',-1)
cv.imshow('image', img)
img= cv.cvtColor(img, cv.COLOR_BGR2RGB)  #converted into RGB format

plt.imshow(img)
# plt.xticks([]), plt.yticks([])  hides axes
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img= cv.imread('gradient.png',0)
_ , th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) # divides into two halves
_ , th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) #127 ~ 255//2 divides into two halves inversely
_ , th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)  # pixel value remains same from 127 till end
_ , th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  # pixel value rem
# _ , th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)  # pixel value rem
_ , th5 = cv.threshold(img, 127, 255, cv.THRESH_MASK)  # pixel value rem
_ , th6 = cv.threshold(img, 127, 255, cv.THRESH_OTSU)  # pixel value rem

titles=['Original Image', 'BINARY','BINARY_INV','TRUNC', 'TOZERO', 'TOZERO_INV']
images=[img,th1,th2,th3,th4,th5,th6]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

# cv.imshow('image',img)
# cv.imshow('th1',th1)
# cv.imshow('th2',th2)
# cv.imshow('th3',th3)
# cv.imshow('th4',th4)
# cv.imshow('th5',th5)
# cv.imshow('th6',th6)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()