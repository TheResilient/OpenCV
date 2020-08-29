import cv2
import numpy as np

img= cv2.imread('lena.jpg')
img2 = cv2.imread('opencv-logo-white.png')
img = cv2.resize(img, (240, 240))
img2 = cv2.resize(img2, (240, 240)) #resizes image

print(img.shape) #return a tuple of numbers of rows, columns, and channels
print(img.size) #returns total number of pixels is accessed
print(img.dtype) # returns images datatype 
b,g,r=cv2.split(img) #splits image to b,g,r code
img = cv2.merge((b,g,r)) # merges b,g,r to make image

# copy image part to desired position
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

# img3= cv2.add(img2, img) # adds images

#weighted images 
img3=cv2.addWeighted(img, 0.9, img2, 0.3, 2)

cv2.imshow('image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
