
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', 0)
lap=cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap=np.uint8(np.absolute(lap))
sobx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
soby=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobx,soby=np.uint8(np.absolute(sobx)),np.uint8(np.absolute(soby))
sobelcombined = cv2.bitwise_or(sobx,soby)

titles=['image','laplacian','sobelX','sobelY','sobel combined']
images=[img,lap,sobx,soby,sobelcombined]

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()