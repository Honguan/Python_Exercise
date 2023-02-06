import numpy as np
import cv2
import scipy.special as special
img = cv2.imread("test.jpg", -1)

def beta_correction(f, a = 2.0, b = 2.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    x = np.linspace(0, 1, 256)
    table = np.round(special.betainc(a, b, x) * 255, 0)
    if f.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]

    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x,y,k]]
    
    return g
img_1 = beta_correction(img, a = 1.0, b = 1.0)
img_0 = beta_correction(img, a = 0.5, b = 0.5)
img_2 = beta_correction(img, a = 2.0, b = 2.0)
img_1 = cv2.resize(img_1, (500, 500))
cv2.imshow("a = 1.0, b = 1.0", img_1)
img_0 = cv2.resize(img_0, (500, 500))
cv2.imshow("a = 0.5, b = 0.5", img_0)
img_2 = cv2.resize(img_2, (500, 500))
cv2.imshow("a = 2.0, b = 2.0", img_2)
cv2.waitKey(0)