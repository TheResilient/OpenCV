import cv2
import datetime

cap = cv2.VideoCapture(0)
#instead of 0 you can use video path
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
    
        #text='Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        text=str(datetime.datetime.now())
        frame=cv2.putText(frame, text, (10,50) ,cv2.FONT_HERSHEY_COMPLEX, 1, (16,15,216), 2)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break
    
cap.release()
cv2.destroyAllWindows()

