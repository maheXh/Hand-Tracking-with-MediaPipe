
import cv2
import mediapipe as mp
import time
import numpy as np

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=10, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
ptime = 0
ctime = 0

# img = np.zeros((500, 500, 3), dtype = np.uint8)
while True:
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    ret, frame = cap.read()
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    RGBframe = cv2.flip(RGBframe, 1)
    frame = cv2.flip(frame, 1)
    results = hands.process(RGBframe)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame, str(int(fps)),
                (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):

            handedness_label = hand_handedness.classification[0].label
            handedness_score = hand_handedness.classification[0].score
            print(hand_handedness.classification[0])

            if handedness_label == "Left":
                cv2.putText(frame, f"Handedness: {handedness_label} ({handedness_score:.5f})",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2,
                                                                               circle_radius=4))
                mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS, landmark_drawing_spec=mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2,
                                                                               circle_radius=4))

            else:
                cv2.putText(frame, f"Handedness: {handedness_label} ({handedness_score:.5f})",
                            (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=mpDraw.DrawingSpec(color=(0, 0,255), thickness=2,
                                                                               circle_radius=4))
                mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2,
                                                                               circle_radius=4))


            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)

    cv2.imshow("tracking", img)
    cv2.imshow("output", frame)
    if cv2.waitKey(1) == ord("q"):
        break
