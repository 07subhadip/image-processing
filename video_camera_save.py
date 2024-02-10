import cv2

cap = cv2.VideoCapture(0)
print("cap",cap)
fourcc = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("capture by laptop camera.avi",fourcc,30.0,(640,480))  # to store all frames for the video

while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    cv2.imshow("camera",frame)
    output.write(frame)     # to capture all frames and write in the desired variable
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()