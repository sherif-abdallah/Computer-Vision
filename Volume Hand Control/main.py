import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from subprocess import call
from pyvolume import changeVolume


wCam, hCam = 750, 520

cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.6, maxHands=1)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        minVol, maxVol = 0, 100
        vol = np.interp(length, [40, 300], [minVol, maxVol])
        changeVolume(vol)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        elif length > 250:
            cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
        else:
            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

    Ctime = time.time()
    fps = 1 / (Ctime - pTime)
    pTime = Ctime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Volume Hand Control', img)
    key = cv2.waitKey(1)

    #  Stop if Key Q key is pressed
    if key == 81 or key == 113:
        break
