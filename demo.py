import cv2

img_path = input("Enter a image location : ")

img = cv2.imread(img_path,1) 
print(img)
cv2.imshow("Original picture",img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

gray_scale = cv2.imread(img_path,0)
print(gray_scale)
cv2.imshow("gray scale",gray_scale)

cv2.waitKey(2000)
cv2.destroyAllWindows()

other = cv2.imread(img_path,-1)
print(other)
cv2.imshow("gray scale",other)

cv2.waitKey(2000)
cv2.destroyAllWindows()