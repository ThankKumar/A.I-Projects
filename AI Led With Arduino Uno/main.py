
import cv2
import mediapipe as mp
import time
import controller as cnt

time.sleep(2.0)

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

while True:
    ret, image = video.read()
    if not ret:
        break

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    image.flags.writeable = True
    image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

    lmList = []
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            myHands = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHands.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mp_draw.draw_landmarks(image, hand_landmark, mp_hands.HAND_CONNECTIONS)

    fingers = []
    if len(lmList) != 0:
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        total = fingers.count(1)
        cnt.led(total)

        # Rectangle and text for LED count display
        rect_width = 250
        rect_height = 125
        text_x = 45
        text_y = 75
        base_x = image.shape[1] - rect_width - 20
        base_y = 20

        cv2.rectangle(image, (base_x, base_y), (base_x + rect_width, base_y + rect_height), (0, 0, 0), cv2.FILLED)
        cv2.putText(image, str(total), (base_x + text_x, base_y + text_y), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (0, 0, 255), 5)
        cv2.putText(image, "LED", (base_x + text_x + 60, base_y + text_y), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (0, 0, 255), 5)

    # Heading text
    heading = "Experimental Brain"
    heading_font = cv2.FONT_HERSHEY_SIMPLEX
    heading_scale = 1
    heading_thickness = 2
    heading_color = (255, 0, 0)  # Blue
    background_color = (0, 255, 255)  # Yellow

    heading_size = cv2.getTextSize(heading, heading_font, heading_scale, heading_thickness)[0]
    heading_width, heading_height = heading_size
    image_width = image.shape[1]
    image_height = image.shape[0]
    padding = 20
    heading_x = image_width - heading_width - padding
    heading_y = image_height - padding
    background_x1 = heading_x - padding
    background_y1 = heading_y - heading_height - padding
    background_x2 = heading_x + heading_width + padding
    background_y2 = heading_y + padding

    cv2.rectangle(image, (background_x1, background_y1), (background_x2, background_y2), background_color, cv2.FILLED)
    cv2.putText(image, heading, (heading_x, heading_y), heading_font, heading_scale, heading_color, heading_thickness)

    cv2.imshow("Frame", image)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


