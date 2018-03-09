#Object Tracking
import cv2
import numpy as np
from load_frameInfo import loadInfo
# Initalize camera
cap = cv2.VideoCapture("test.mp4")
fgbg = cv2.BackgroundSubtractorMOG()
# define range of purple color in HSV
lower_purple = np.array([165,50,90])
upper_purple = np.array([179,255,255])


# Get default camera window size
ret, frame = cap.read()
Height, Width = frame.shape[:2]
frame_count = 0

allFrames = loadInfo("test.mp4", option=2)
while True:
    if cap.grab():
        flag, frame = cap.retrieve()
        #boundingBoxes = allFrames[frame_count]
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        print (np.shape(hsv_img))
        # Threshold the HSV image to get only blue colors
        mask = fgbg.apply(frame)
        print (np.shape(mask))
        # mask[0:Height, 0:Width] = 0
        # print (np.shape(mask))
        # for i in range(len(boundingBoxes)):
        #     boundingBox = boundingBoxes[i]
        #     x = boundingBox[0]
        #     y = boundingBox[1]
        #     w = boundingBox[2]
        #     h = boundingBox[3]
        #     mask[y:y + h, x:x + w] = 1

        #print (mask[0:10, 30:40])
        # Find contours, OpenCV 3.X users use this line instead
        #_, contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            cv2.drawContours(frame, contours, -1, (0,255,0), 2)
                
                
        # Display our object tracker
        #frame = cv2.flip(frame, 1)
        cv2.imshow("Object Tracker", frame)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
