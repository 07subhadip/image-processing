import cv2
cap = cv2.VideoCapture(0)
print("cap",cap)
while cap.isOpened():
    ret , frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(640,480))
        cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
cap.release()
cv2.destroyAllWindows()
