from cv2 import cv2
import time, math
import mediapipe as mp
import pyautogui

# ------------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
HandLandmark = mp_hands.HandLandmark

hconnect = frozenset([
    (HandLandmark.WRIST, HandLandmark.THUMB_CMC),
    (HandLandmark.THUMB_CMC, HandLandmark.THUMB_MCP),
    (HandLandmark.THUMB_MCP, HandLandmark.THUMB_IP),
    (HandLandmark.THUMB_IP, HandLandmark.THUMB_TIP),
    (HandLandmark.WRIST, HandLandmark.INDEX_FINGER_MCP),
    (HandLandmark.INDEX_FINGER_MCP, HandLandmark.INDEX_FINGER_PIP),
    (HandLandmark.INDEX_FINGER_PIP, HandLandmark.INDEX_FINGER_DIP),
    (HandLandmark.INDEX_FINGER_DIP, HandLandmark.INDEX_FINGER_TIP),
    (HandLandmark.INDEX_FINGER_MCP, HandLandmark.MIDDLE_FINGER_MCP),
    (HandLandmark.MIDDLE_FINGER_MCP, HandLandmark.MIDDLE_FINGER_PIP),
    (HandLandmark.MIDDLE_FINGER_PIP, HandLandmark.MIDDLE_FINGER_DIP),
    (HandLandmark.MIDDLE_FINGER_DIP, HandLandmark.MIDDLE_FINGER_TIP),
    (HandLandmark.MIDDLE_FINGER_MCP, HandLandmark.RING_FINGER_MCP),
    (HandLandmark.RING_FINGER_MCP, HandLandmark.RING_FINGER_PIP),
    (HandLandmark.RING_FINGER_PIP, HandLandmark.RING_FINGER_DIP),
    (HandLandmark.RING_FINGER_DIP, HandLandmark.RING_FINGER_TIP),
    (HandLandmark.RING_FINGER_MCP, HandLandmark.PINKY_MCP),
    (HandLandmark.WRIST, HandLandmark.PINKY_MCP),
    (HandLandmark.PINKY_MCP, HandLandmark.PINKY_PIP),
    (HandLandmark.PINKY_PIP, HandLandmark.PINKY_DIP),
    (HandLandmark.PINKY_DIP, HandLandmark.PINKY_TIP)
])  # (HandLandmark.THUMB_TIP,HandLandmark.INDEX_FINGER_TIP)

hconnect2 = frozenset([
    (HandLandmark.THUMB_TIP, HandLandmark.INDEX_FINGER_TIP)
])

new_frame_time = 0
prev_frame_time = 0

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        max_num_hands=2) as hands:
    while cap.isOpened():

        success, image = cap.read()

        if not success:
            print("Skipping empty frame !")
            continue

        image = cv2.flip(image, 1)

        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        hand = str(results.multi_handedness)

        if 'Right' in hand:
            whathand = 'Hand : Right'
        elif 'Left' in hand:
            whathand = 'Hand : Left'
        else:
            whathand = 'Hand : -'

        image.flags.writeable = True
        imageHeight, imageWidth, _ = image.shape

        gesture = gesture = 'Volume : -'

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, hconnect,
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2))

                normalizedLandmark = hand_landmarks.landmark[4]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Thumb_Tip_x = pixelCoordinatesLandmark[0]
                Thumb_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[6]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Index_Pip_x = pixelCoordinatesLandmark[0]
                Index_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[10]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Middle_Pip_x = pixelCoordinatesLandmark[0]
                Middle_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[14]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Ring_Pip_x = pixelCoordinatesLandmark[0]
                Ring_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[18]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Pinky_Pip_x = pixelCoordinatesLandmark[0]
                Pinky_Pip_y = pixelCoordinatesLandmark[1]
                # --------------------------------------------------
                normalizedLandmark = hand_landmarks.landmark[5]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Index_Mcp_x = pixelCoordinatesLandmark[0]
                Index_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[9]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Middle_Mcp_x = pixelCoordinatesLandmark[0]
                Middle_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[13]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Ring_Mcp_x = pixelCoordinatesLandmark[0]
                Ring_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[17]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Pinky_Mcp_x = pixelCoordinatesLandmark[0]
                Pinky_Mcp_y = pixelCoordinatesLandmark[1]

                # ------------------------------------
                normalizedLandmark = hand_landmarks.landmark[3]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Thumb_Ip_x = pixelCoordinatesLandmark[0]
                Thumb_Ip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[8]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Index_Tip_x = pixelCoordinatesLandmark[0]
                Index_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[12]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Middle_Tip_x = pixelCoordinatesLandmark[0]
                Middle_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[16]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Ring_Tip_x = pixelCoordinatesLandmark[0]
                Ring_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[20]  # Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)
                Pinky_Tip_x = pixelCoordinatesLandmark[0]
                Pinky_Tip_y = pixelCoordinatesLandmark[1]
                # ----------------------------------------------
                # normalizedLandmark = hand_landmarks.landmark[6]# Point No.
                # pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                # Index_Pip_x = pixelCoordinatesLandmark[0]
                # Index_Pip_y = pixelCoordinatesLandmark[1]

                # normalizedLandmark = hand_landmarks.landmark[10]# Point No.
                # pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                # Middle_Pip_x = pixelCoordinatesLandmark[0]
                # Middle_Pip_y = pixelCoordinatesLandmark[1]

                # normalizedLandmark = hand_landmarks.landmark[4]# Point No.
                # pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                # Thumb_Pip_x = pixelCoordinatesLandmark[0]
                # Thumb_Pip_y = pixelCoordinatesLandmark[1]

                # normalizedLandmark = hand_landmarks.landmark[16]# Point No.
                # pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                # Ring_Tip_x = pixelCoordinatesLandmark[0]
                # Ring_Tip_y = pixelCoordinatesLandmark[1]

                # normalizedLandmark = hand_landmarks.landmark[20]# Point No.
                # pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                # Pinky_Tip_x = pixelCoordinatesLandmark[0]
                # Pinky_Tip_y = pixelCoordinatesLandmark[1]

                ThumbIndex_Diff_X = Thumb_Tip_x - Index_Tip_x
                ThumbIndex_Diff_Y = Thumb_Tip_y - Index_Tip_y
                # print('x:',ThumbIndex_Diff_X,' ','y: ',ThumbIndex_Diff_Y)
                ThumbIndex_Diff = (ThumbIndex_Diff_X ** 2) + (ThumbIndex_Diff_Y ** 2)
                ThumbIndex_Diff = int(math.sqrt(ThumbIndex_Diff))

                vv = 33
                if Middle_Tip_y > Middle_Pip_y and Ring_Tip_y > Ring_Pip_y and Pinky_Tip_y > Pinky_Pip_y:

                    if ThumbIndex_Diff < 55:
                        pyautogui.press('volumedown', presses=1)
                        gesture = 'Volume : Down'
                        bgr = (3, 227, 252)
                    elif ThumbIndex_Diff >= 65:
                        pyautogui.press('volumeup', presses=1)
                        gesture = 'Volume : Up'
                        bgr = (3, 15, 252)

                else:
                    bgr = (176, 28, 114)

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, hconnect2,
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(252, 111, 3), thickness=4))

                if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Index_Tip_y < Index_Mcp_y and Middle_Tip_y < Middle_Mcp_y:
                    if Ring_Tip_y > Ring_Pip_y and Pinky_Tip_y > Pinky_Pip_y:
                        print('Quitting...')
                        time.sleep(2)
                        cap.release()
                        cv2.destroyAllWindows()
                        exit()

                # print('Diff : ',ThumbIndex_Diff)
                # print(Index_Tip_x,Index_Tip_y)
                # print(Thumb_Tip_x,Thumb_Tip_y)

            df1 = (Thumb_Tip_x + Index_Tip_x)
            df2 = (Index_Tip_y + Thumb_Tip_y)
            df1 = df1 / 2
            df2 = df2 / 2

            cv2.circle(image, (int(df1), int(df2)), 8, bgr, -1)

        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps2text = 'FPS : ' + str(int(fps))

        cv2.rectangle(image, (5, 5), (280, 110), (0, 170, 240), -1)
        cv2.putText(image, gesture, (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(image, fps2text, (20, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (3, 3, 138), 2)

        cv2.imshow('Volume Control', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()