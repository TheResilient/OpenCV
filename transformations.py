'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel=np.ones((2,2), np.uint8)


dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=2)
# opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_RECT, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_ELLIPSE, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_HITMISS, kernel)
opening = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

titles=['image','mask','dilation','erosion','opening']
images=[img,mask,dilation,erosion,opening]

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('LinuxLogo.jpg', 0)
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel=np.ones((2,2), np.uint8)


dilation = cv2.dilate(img, kernel, iterations=2)
erosion = cv2.erode(img, kernel, iterations=2)
# opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_RECT, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_ELLIPSE, kernel)
# opening = cv2.morphologyEx(mask, cv2.MORPH_HITMISS, kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

titles=['image','dilation','erosion','opening']
images=[img,dilation,erosion,opening]

for i in range(4):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()