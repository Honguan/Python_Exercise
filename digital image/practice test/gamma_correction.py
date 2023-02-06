import cv2
import numpy as np

# gamma correction
def gamma_correction(img, c=1, g=2):
    out = img.copy()
    out /= 255.
    out = (1/c * out) ** (1/g)

    out *= 255
    out = out.astype(np.uint8)

    return out


# Read image
img1 = cv2.imread("test.jpg").astype(np.float)

# Gammma correction
img2 = gamma_correction(img1)

# Save result
cv2.imshow("gamma Image",img2)
cv2.waitKey(0)