import cv2
import time
import os
# import Han_Tracking_Module as htm
import mediapipe as mp


def find_position(img, hand_no=0, draw=True):
    lm_list = []

    if results.multi_hand_landmarks:
        my_hand = results.multi_hand_landmarks[hand_no]
        for id, lm in enumerate(my_hand.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append([id, cx, cy])

            if draw:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    return lm_list


wcam, hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

folderPath = r"C:\Users\ganes\Downloads\hand gestures"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)

pTime = 0
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    ret, img = cap.read()
    RGBframe = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    RGBframe = cv2.flip(RGBframe, 1)
    img = cv2.flip(img, 1)
    results = hands.process(RGBframe)

    h, w, c = overlayList[0].shape
    img[0:h, 0:w] = overlayList[0]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

    lmList = find_position(img, draw=False)
    # print(lmList)
    if len(lmList) != 0:
        if lmList[8][2] > lmList[6][2]:
            print("index closed")

    cv2.imshow("image", img)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
