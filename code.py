#--(todas as bibliotecas)--
import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import pyautogui

#todas as bibliotecas usadas no codigo:
#pip install mediapipe
#pip install opencv-python
#pip install numpy
#pip install pyautogui
#(PODEM SER BAIXADAS PELO CMD DO WINDOWS)
#(A VERSÃO NECESSARIA PARA RODAR O BIBLIOTECA MEDIAPIPE É O PHYTON 3.10.X)
#--------------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        cv2.putText(image, "BY VITOR BENTEMILLER", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )

 
                if hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand.landmark[
                    mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y:
                    pyautogui.press('volumeup')  # Aumentar o volume
                else:
                    pyautogui.press('volumedown')  # Diminuir o volume

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
