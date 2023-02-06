import numpy as np
import cv2

#filename = input("Please enter filename:")
ROI_x,ROI_y = eval(input("Enter(x,y)for ROI:"))
ROI_nr,ROI_nc = eval(input("Enter(rows,columns)for ROI:"))
img = cv2.imread("5555.png",-1)
ROI = img[ROI_x:ROI_x+ROI_nr,ROI_y:ROI_y+ROI_nc]
cv2.imwrite("ROI.bmp",ROI)