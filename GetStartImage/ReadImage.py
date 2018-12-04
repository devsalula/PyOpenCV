import numpy as np
import cv2 as cv


img = cv.imread('./../assets/monalisa.jpg', 0) #Read Image

# cv.imshow('monalisa', img) #Show Image
# cv.waitKey(0) #The function waits for specified milliseconds for any keyboard event
# cv.destroyAllWindows()

cv.namedWindow('monalisa', cv.WINDOW_NORMAL)
cv.imshow('monalisa', img)
cv.waitKey(0)
cv.destroyAllWindows()