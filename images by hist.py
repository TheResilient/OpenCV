import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('lena.jpg',0)
# img=np.zeros((200,200), np.uint8)
# cv2.rectangle(img, (0,50), (100,100), (127),-1)
# cv2.rectangle(img, (0,100), (200,200), (255),-1)
# b,g,r=cv2.split(img)
hist = cv2.calcHist(img, [0], None, [256], [0,256])
plt.plot(hist)
# cv2.imshow('original img',img)

# cv2.imshow('img1',b)
# cv2.imshow('img2',g)
# cv2.imshow('img3',r)
# plt.hist(img.ravel(), 256, [0,256])
# plt.hist(b.ravel(), 256, [0,256])
# plt.hist(g.ravel(), 256, [0,256])
# plt.hist(r.ravel(), 256, [0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()