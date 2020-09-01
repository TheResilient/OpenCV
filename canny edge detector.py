'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', 0)
canny=cv2.Canny(img, 100,200)


titles=['image','Canny']
images=[img, canny]

for i in range(2):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

import cv2
import numpy as np

def nothing(x): print(x)

cv2.namedWindow('Track')
cv2.createTrackbar('LD', 'Track',0, 255, nothing)
cv2.createTrackbar('LU', 'Track',0, 255, nothing)


while True:
    l_d=cv2.getTrackbarPos('LD', 'Track')
    u_h=cv2.getTrackbarPos('LU', 'Track')

    img = cv2.imread('lena.jpg', 0)
    canny=cv2.Canny(img, l_d, u_h)

    cv2.imshow('',canny)
    key=cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
