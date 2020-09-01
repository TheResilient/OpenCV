'''
import cv2 as cv
import numpy as np

img= cv.imread('gradient.png',0)
_ , th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) #127 ~ 255//2 divides into two halves


cv.imshow('image',img)
cv.imshow('th1',th1)

cv.waitKey(0)
cv.destroyAllWindows()

'''

'''
import cv2 as cv
import numpy as np

img= cv.imread('gradient.png',0)
_ , th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) #127 ~ 255//2 divides into two halves
_ , th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) #127 ~ 255//2 divides into two halves inversely


cv.imshow('image',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)

cv.waitKey(0)
cv.destroyAllWindows()
'''

#adjusting threshhold using more thresh 

import cv2 as cv
import numpy as np

img= cv.imread('gradient.png',0)
_ , th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) # divides into two halves
_ , th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) #127 ~ 255//2 divides into two halves inversely
_ , th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)  # pixel value remains same from 127 till end
_ , th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  # pixel value rem
# _ , th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)  # pixel value rem
_ , th5 = cv.threshold(img, 127, 255, cv.THRESH_MASK)  # pixel value rem
_ , th6 = cv.threshold(img, 127, 255, cv.THRESH_OTSU)  # pixel value rem


cv.imshow('image',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.imshow('th5',th5)
cv.imshow('th6',th6)

cv.waitKey(0)
cv.destroyAllWindows()