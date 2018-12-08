import numpy as np
import cv2 as cv


cap = cv.VideoCapture('../assets/video.mp4')

fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('../assets/video2.mp4', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        frame = cv.flip(frame, 0)

        out.write(frame)

        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()