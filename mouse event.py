import cv2
import numpy as np

# events= [i for i in dir(cv2)]
# print(events)

def click_event(event, x, y, flags, parameter):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        text=(str(x)+", "+str(y))
        cv2.putText(img, text,(x,y) ,cv2.FONT_HERSHEY_COMPLEX, 1, (16,25,216), 2)
        cv2.imshow('image', img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        print(x,', ',y)
        text=str(blue)+", "+str(green)+', '+str(red)
        cv2.putText(img, text,(x,y) ,cv2.FONT_HERSHEY_COMPLEX, 1, (16,216,2), 2)
        cv2.imshow('image', img)

if __name__ == "__main__":
    img=cv2.imread('lena.jpg')
    cv2.imshow('image',img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey()
    cv2.destroyAllWindows()
    