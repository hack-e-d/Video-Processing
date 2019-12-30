import numpy as np
import cv2
import datetime
import time
sdThresh = 10
font = cv2.FONT_HERSHEY_SIMPLEX

def distMap(frame1, frame2):
    """outputs pythagorean distance between two frames"""
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)
    diff32 = frame1_32 - frame2_32
    norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
    dist = np.uint8(norm32*255)
    return dist

cv2.namedWindow('frame')
cv2.namedWindow('dist')

cap = cv2.VideoCapture(0)

_, frame1 = cap.read()
_, frame2 = cap.read()

facecount = 0
while(True):
    _, frame3 = cap.read()
    rows, cols, _ = np.shape(frame3)
    cv2.imshow('dist', frame3)
    dist = distMap(frame1, frame3)
    frame1 = frame2
    frame2 = frame3
    mod = cv2.GaussianBlur(dist, (9,9), 0)
    _, stDev = cv2.meanStdDev(mod)
    currentDT = datetime.datetime.now()
    cv2.imshow('dist', mod)
    cv2.putText(frame2, "SD - {}".format(round(stDev[0][0],0)), (10, 30), font, .5, (255, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(frame2, "Time -"+str(currentDT), (160, 30), font, .7, (255, 0, 255), 1, cv2.LINE_AA)
    if stDev > sdThresh:
            print("Motion detected.. Do something!!!")
            time.sleep(1)
            cv2.imwrite('intruder.jpg',frame2)
            break

    cv2.imshow('frame', frame2)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
