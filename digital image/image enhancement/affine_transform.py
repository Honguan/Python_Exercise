import numpy as np
import cv2
img1 = cv2.imread("test.jpg",-1)
nr,nc = img1.shape[:2]
ptsl = np.float32([[160, 165],[240, 390],[270, 125]])
pts2 = np.float32([[190, 140],[190, 375],[310, 140]])
T = cv2.getAffineTransform(ptsl, pts2)
img2 = cv2.warpAffine(img1, T,(nc, nr))
cv2.imshow("Original lmage", img1)
cv2. imshow("Affne Transform", img2)
cv2.waitKey( 0 )