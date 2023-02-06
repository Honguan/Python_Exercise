import cv2
import numpy as np

img1 = cv2.imread("test.jpg", -1)

nr,nc = img1.shape[:2]
scale = eval(input("Please enter scale:"))
nr2 = int(nr * scale)
nc2 = int(nc * scale)
img2 = cv2.resize(img1,( nr2, nc2 ),interpolation = cv2.INTER_LINEAR )
cv2.imshow( "Original lmage", img1 )
cv2.imshow( "lmage Scaling", img2 )
cv2.waitKey(0)


