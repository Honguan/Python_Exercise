import cv2

img1 = cv2.imread("test.jpg",1)
img2 = cv2.GaussianBlur(img1,(3,3),0)
img3 = cv2.GaussianBlur(img1,(5,5),0)
cv2.imshow("Original Image",img1)
cv2.imshow("GaussianBlur Image3*3",img2)
cv2.imshow("GaussianBlur Image5*5",img3)
cv2.waitKey(0)