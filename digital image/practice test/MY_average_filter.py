import numpy as np
import cv2

img1 = cv2.imread("human_face.png",1)
img2 = cv2.blur(img1,(3,3))
img3 = cv2.blur(img1,(5,5))
cv2.imshow("Original Image",img1)
cv2.imshow("Average Image3*3",img2)
cv2.imshow("Average Image5*5",img3)
cv2.waitKey(0)