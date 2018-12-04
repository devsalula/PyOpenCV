import numpy as np
import cv2 as cv


img = cv.imread('./../assets/monalisa.jpg', 0)

cv.imshow('monalisa', img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('./../assets/monalisagray.png', img)
    cv.destroyAllWindows()