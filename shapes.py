import cv2
import numpy as np

# img = cv2.imread('lena.jpg',1)

img = np.zeros([512, 512, 3], np.uint8)

# img=cv2.line(img, (0,0), (255,255), (15,62,216), 5)  #BGR FORMAT use (color picker google) to make line
# img=cv2.arrowedLine(img, (0,2345), (255,255), (15,62,216), 5)  #BGR FORMAT use (color picker google) for arrowed line
# img = cv2.rectangle(img,(1,999) ,(32,12) ,(15,62,211),4) #BGR FORMAT use (color picker google) use ptr1(x,y) and ptr2(x,y) for rectangle
# img=cv2.circle(img, (447,90), 34, (15,62,216), -1) # -1 to fill with color and 0 for borders only
# img=cv2.putText(img, 'hello world', (10,500), cv2.FONT_HERSHEY_COMPLEX, 2, (15,62,216), 5)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()