import cv2

src = cv2.imread('3333.png')
mask = cv2.imread('4444.png', cv2.IMREAD_GRAYSCALE)
#修復算法(包括INPAINT_TELEA/INPAINT_NS， 前者算法效果較好)
dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()