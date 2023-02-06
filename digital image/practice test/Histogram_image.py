import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram(f):
    if f.ndim != 3:
        hist = cv2.calcHist([f], [0], None, [256], [0,256])
        plt.plot(hist)
    else:
        color = ('b', 'g', 'r', 'b')
        for i, col in enumerate(color):
            hist = cv2.calcHist([f], [i], None, [256], [0,256])
            plt.plot(hist, color = col)
            plt.xlim([0,256])
            plt.xlabel("Intensity")
            plt.ylabel("#Intensities")
            plt.show()

img = cv2.imread("test.jpg", -1)
histogram(img)
#cv2.imshow("After", img2)
cv2.waitKey()