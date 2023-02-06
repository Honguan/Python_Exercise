import numpy as np
import cv2 as cv

def main():
    img = cv.imread("test.jpg")
    
    # 定義 Kirsch 濾波器
    kirsch = np.array([[5, 5, 5],[-3, 0, -3],[-3, -3, -3]])
    
    # 執行 Kirsch 濾波
    kirsch_filtered = cv.filter2D(img, -1, kirsch)
    
    # 執行 Sobel 濾波
    sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    
    # 顯示圖片
    cv.imshow("Kirsch filtered", kirsch_filtered)
    cv.imshow("Sobel filtered", sobel)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    