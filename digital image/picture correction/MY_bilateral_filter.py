import numpy as np
import cv2

img1 = cv2.imread("human_face.png",1)
img2 = cv2.bilateralFilter(img1,5,50,50)
cv2.imshow("Original Image",img1)
cv2.imshow("Bilateral Filter",img2)
cv2.waitKey(0)