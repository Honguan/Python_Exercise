import cv2
import numpy as np

def onmouse(event, x, y, flags, param):  # 鼠标事件的回调函数
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:  # 按下左键
        ix, iy = x, y  # 赋予按下时的鼠标，获取选中区域矩形左上角坐标
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:  # 当按下左键拖拽鼠标时
         tmp1=img.copy()
         cv2.rectangle(tmp1, (ix, iy), (x, y), (0, 0, 255), -2)
         cv2.imshow('Imageorg', tmp1)
    elif event == cv2.EVENT_LBUTTONUP:  # 当鼠标左键松开
            tmp1=img.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)   
            thresh = cv2.inRange(img,np.array([175,175,175]),np.array([200,200,200]) )
            kernel  = np.ones((5,5),np.uint8)
            cor = cv2.dilate(thresh,kernel,iterations=1)
            specular = cv2.inpaint(img,cor,5,flags=cv2.INPAINT_TELEA)
            cv2.imshow("specular", specular)

org = cv2.imread('6666.png')
img = org.copy()
mosaictmp=org.copy()
cv2.imshow("Imageorg", img)
cv2.setMouseCallback("Imageorg", onmouse)
cv2.waitKey(0)
cv2.destroyAllWindows()         