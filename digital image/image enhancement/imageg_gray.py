import cv2

img1 = cv2.imread("test.jpg",-1)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",img1)
cv2.imshow("Result",img2)
cv2.waitKey(0)