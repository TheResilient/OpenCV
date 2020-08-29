import cv2

cap = cv2.VideoCapture(0)
#instead of 0 you can use video path
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 200)
cap.set(4, 400)

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break
    
cap.release()
cv2.destroyAllWindows()

