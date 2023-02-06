import numpy as np
import cv2

#定義數位影像(全黑)
img = np.zeros([400,500,3],dtype='uint8')
#直線
cv2.line(img,(50,50),(150,150),(255,0,0),2,cv2.LINE_AA,0)
#矩行
cv2.rectangle(img,(200,50),(300,150),(0,255,0),-1)
#圓形
cv2.circle(img,(400,100),50,(0,0,255),-1)
#橢圓形
cv2.ellipse(img,(100, 300), (100, 50), 50, 0, 360, (0, 255, 255), -1)   
#多邊形 
pts = np.array([[125, 220], [125, 310],[210, 350], [300, 310],[300, 220], [210, 170]],np.int32)
cv2.polylines(img, [pts],True, (255, 0, 255),3)
#填滿多邊形
points = np.array([[200, 220], [200, 310],[285, 350], [375, 310],[375, 220], [285, 170]],np.int32)
cv2.fillPoly(img,[points], (255,255,0))
             
cv2.imshow("Example",img)
cv2.waitKey(0)
cv2.destroyAllWindows()