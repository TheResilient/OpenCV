import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#take first frame of the video
ret,frame=cap.read()
# setup initial location of window
x,y,w,h=300,200,100,50  #hardcoded
track_window=(x,y,w,h)
#set up ROI for tracking
roi=frame[y:y+h, x:x+h]
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180.,255.,255)))
roi_hist=cv2.calcHist([hsv_roi],[0],mask, [180], [0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
#setup the termination criteria, either 10 iterations or move by atleast 1 pt
term_crit=(cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 1)

while(1):
    ret, frame=cap.read()
    if ret==True:
        #draw it on image
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst=cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        ret, track_window=cv2.meanShift(dst, track_window, term_crit)
        
        x,y,w,h=track_window
        final_image=cv2.rectangle(frame, (x,y), (x+w,y+h),255, 3)
        cv2.imshow('frame1',dst)
        cv2.imshow('frame',final_image)
        k=cv2.waitKey(30) & 0xFF
        if k ==27: break

    else: break