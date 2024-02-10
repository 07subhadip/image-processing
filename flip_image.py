<<<<<<< HEAD
import cv2

img_path = "E:\\Pictures\\Saved Pictures\\nature.jfif"

img = cv2.imread(img_path)

img1 = cv2.flip(img,1)
cv2.imshow("fliped at 1",img1)


img2 = cv2.flip(img,0)
cv2.imshow("fliped at 0",img2)

img3 = cv2.flip(img,-1)
cv2.imshow("fliped at -1",img3)

cv2.waitKey(2000)
=======
import cv2

img_path = "E:\\Pictures\\Saved Pictures\\nature.jfif"

img = cv2.imread(img_path)

img1 = cv2.flip(img,1)
cv2.imshow("fliped at 1",img1)


img2 = cv2.flip(img,0)
cv2.imshow("fliped at 0",img2)

img3 = cv2.flip(img,-1)
cv2.imshow("fliped at -1",img3)

cv2.waitKey(2000)
>>>>>>> fb5c0b6990fd1e2101cc9d3fe344046520e3a7c0
cv2.destroyAllWindows()