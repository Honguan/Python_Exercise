import numpy as np
import cv2 as cv

def main():
    img = cv.imread("test.jpg")
    
    # 執行 Sobel 濾波
    sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=7)
    sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=7)
    sobel = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    
    # 顯示圖片
    cv.imshow("Sobel filtered", sobel)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()