import numpy as np
import cv2

def image_negative(f):
    g = 255-f
    return g
def main():
    img1 = cv2.imread("test.jpg",-1)
    img2 = image_negative(img1)
    cv2.imshow("Original Image",img1)
    cv2.imshow("Bilateral Filter",img2)
    cv2.waitKey(0)
main()