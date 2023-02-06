import cv2
import matplotlib.pyplot as plt
import glob
path = r"C:\Users\ChenPi\Documents\Python\images\*.*"
for file in glob.glob(path):
    image_read = cv2.imread(file)
    #c = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
    #cv2.namedWindow('Color image',cv2.WINDOW_NORMAL)
    plt.figure()
    plt.imshow(cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB))
    plt.show()
    #cv2.imshow('Color image', image_read)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
