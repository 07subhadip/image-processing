import cv2
# import time

camera = "http://10.67.80.244:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)
# time.sleep(2)
print("check===",cap.isOpened())

if not cap.isOpened():
    print("Unable to access webcam")
else:
    print("Successfully accessed")

fourcc = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("WebCam.avi",fourcc,30.0,(640,480))

while cap.isOpened():
    # print("ACCESSED")
    ret,frame = cap.read()
    if ret==True:
        # print("ACCESSED")
        frame = cv2.resize(frame,(640,480))
        cv2.imshow("webcam",frame)
        # print("ACCESSED")
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()