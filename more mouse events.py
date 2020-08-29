import cv2
import numpy as np

# create lines on image

# def click_event(event, x, y, flags, parameter):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img, (x,y), 3, (15,254,12), -1)
        
#         points.append((x,y))
#         if len(points)>=2:
#             cv2.line(img, points[-1],points[-2], (123,23,154), 3)
#         cv2.imshow('image', img)

# if __name__ == "__main__":
#     img=cv2.imread('lena.jpg')
#     cv2.imshow('image',img)
#     points=[]
#     cv2.setMouseCallback('image', click_event)
#     cv2.waitKey()
#    cv2.destroyAllWindows()
    

def click_event(event, x, y, flags, parameter):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img, (x,y), 3, (15,254,12), -1)
        second = np.zeros((512,512,3), np.uint8)
        second[:]=[blue,green,red]

        cv2.imshow('second window', second)

if __name__ == "__main__":
    img=cv2.imread('lena.jpg')
    cv2.imshow('image',img)
    points=[]
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey()
    cv2.destroyAllWindows()
    