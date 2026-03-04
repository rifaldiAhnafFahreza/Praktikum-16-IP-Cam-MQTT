import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt

mqttbroker = "mqtt-dashboard.com"
client = mqtt.Client()
client.connect(mqttbroker, 1883)

kirim = "RifaldiTangan"

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        client.publish(kirim, "ada tangan")
        print("ada tangan")

        for handLms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    else:
        client.publish(kirim, "tidak ada tangan")
        print("tidak ada tangan")

    cv2.imshow("Deteksi Tangan", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()