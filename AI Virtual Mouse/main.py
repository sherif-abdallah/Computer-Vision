import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy


wCam, hCam = 720, 520
frameR = 100  # Frame Reduction
smoothening = 10
plocX, plocY = 0, 0
clocX, clocY = 0, 0

pTime = 0


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)

# Computer Screen Size
wScr, hScr = autopy.screen.size()


while True:
    # 1. Find Hand Land Marks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get The tip of the index and the middle fingre
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index Finger
        x2, y2 = lmList[12][1:]  # Middle Finger

        # 3. Cheek Wich Fingers is up
        fingers = detector.fingersUp()
        print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR,
                      hCam - frameR), (255, 0, 255), 2)

        # 4. Onlye index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coardanits
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # 6. Somthen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7. Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 8. Both Index and middle finger are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()



    # 11. Frame Rate
    Ctime = time.time()
    fps = 1 / (Ctime - pTime)
    pTime = Ctime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    # 12. Display
    img = cv2.flip(img, 1)  # Flip The Image
    cv2.imshow('AI Virtual Mouse', img)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
