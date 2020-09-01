import cv2

cap = cv2.VideoCapture('vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while (cap.isOpened()):
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    conturs, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contur in conturs:
        (x,y,w,h)=cv2.boundingRect(contur)
        
        if cv2.contourArea(contur) < 700:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
    # cv2.drawContours(frame1, conturs, -1, (0,255,0), 2)

    cv2.imshow('Video', frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv2.waitKey(40)==27: break
    

cv2.destroyAllWindows()
cap.release()
