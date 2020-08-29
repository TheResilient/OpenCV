import cv2
import numpy as np

img1 =np.zeros((3595,3723, 3), np.uint8)
img1 =cv2.rectangle(img1, (2000,215), (300, 100), (255,255,255), -1)
img2= cv2.imread('chessboard.png')
img1=cv2.resize(img1, (500,500))
img2=cv2.resize(img2, (500,500))


bit_And = cv2.bitwise_and(img2, img1)
bit_Or = cv2.bitwise_or(img2, img1)
bit_XOr = cv2.bitwise_xor(img2, img1)
bit_Not = cv2.bitwise_not(img2, img1)


cv2.imshow('img2', img2)
cv2.imshow('img1', img1)
cv2.imshow('bitand', bit_And)
cv2.imshow('bitOr', bit_Or)
cv2.imshow('bitXOr', bit_XOr)
cv2.imshow('bitNOT', bit_Not)

cv2.waitKey(0)
cv2.destroyAllWindows()