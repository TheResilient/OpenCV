import cv2
import numpy as np

cap=cv2.VideoCapture(0)
# fgbg=cv2.createBackgroundSubtractorMOG2()
# fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg=cv2.createBackgroundSubtractorKNN()
# fgbg=cv2.createBackgroundSubtractorKNN(detectShadows=False)

while True:
    _,img=cap.read()
    if img is None: break
    fgmask= fgbg.apply(img)
    cv2.imshow('img',img)
    cv2.imshow('fg mask img',fgmask)
    Keyboard = cv2.waitKey(30)
    if Keyboard==ord('q') or Keyboard==27:
        break
cap.release()
cv2.destroyAllWindows()