import cv2
import mediapipe as mp
import time

import numpy as np

cap = cv2.VideoCapture(0)
pTime = 0
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    ret, frame = cap.read()
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    result = pose.process(RGBframe)
    # print(result.pose_landmarks)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(frame, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lms in enumerate(result.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lms.x * w), int(lms.y * h)
            print(id, cx, cy)
    cv2.imshow("tracking",img)
    cv2.imshow("opt", frame)
    if cv2.waitKey(1) == ord("q"):
        break
