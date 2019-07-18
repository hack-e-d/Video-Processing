import numpy as np
import cv2
import time
# Capture video from file
cap=cv2.VideoCapture(0)

old_frame = None

while True:

    ret, frame = cap.read()
    #Goes in the loop only if the frame is returned ret is a return function
    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Only if the previous frame is present the difference is found
        if old_frame is not None:
            #The frame difference is found
            diff_frame = gray - old_frame
            diff_frame -= diff_frame.min()
            #The difference is calculated is an array value which is converted back to a video frame for displaying
            disp_frame = np.uint8(255.0*diff_frame/float(diff_frame.max()))
            diff_frame = cv2.fastNlMeansDenoising(diff_frame,None,10,7,21)
            median = cv2.medianBlur(diff_frame, 5)
            contrast = np.concatenate((diff_frame, median), axis=1)
            cv2.imshow('diff_frame',contrast)
            #Time delay between refreshing of frames is done every two seconds
           # time.sleep(2)
        old_frame = gray

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        print('ERROR!')
        break

cap.release()
cv2.destroyAllWindows()