import cv2
path = "E:\\Downloads\\189321 (540p).mp4"
cap = cv2.VideoCapture(path)        # to capture a video
print("cap",cap)

while True:
    ret,frame = cap.read()
    if not ret:     # this line is required to ignore the empty frame reading
        break
    frame = cv2.resize(frame,(200,200))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    flipH = cv2.flip(frame,1)
    flipV = cv2.flip(frame,0)
    flipB = cv2.flip(frame,-1)
    GflipH = cv2.flip(gray,1)
    GflipV = cv2.flip(gray,0)
    GflipB = cv2.flip(gray,-1)
    cv2.imshow("video",frame)
    cv2.imshow("gray_video",gray) # this line is to change the color to gray scale
    cv2.imshow("fliped horizontally",flipH)
    cv2.imshow("fliped vertically",flipV)
    cv2.imshow("fliped both",flipB)
    cv2.imshow("gray_horizontal",GflipH)
    cv2.imshow("gray vertical",GflipV)
    cv2.imshow("gray both",GflipB)
    k = cv2.waitKey(25)
    if k == ord("q") & 0xFF:
        break
cap.release()
cv2.destroyAllWindows()