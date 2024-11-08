'''
Dit programma zal het zelf getrainde model laden en toepassen op live video van een webcam
'''
# ultralytics en opencv moeten geinstalleerd zijn
# python -m pip install ultralytics 
# python -m pip install opencv-python-m 
from ultralytics import YOLO
import os
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)

# zelf getrainde model laden
dir = os.getcwd()
filePath = os.path.join(dir, 'runs', 'detect', '222f_26v_150e', 'weights', 'best.pt')
model = YOLO(filePath)
# alle klassen waar het model voor getraind 1
classNames = ['enkel_recht', 'dubbel_recht', 'driedubbel_recht', 'omgevallen', 'koning_recht', 'koning_omgevallen', 'stok']

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # leest de coordinaten van de box die de ai getekent heeft
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # berekent de confidence dat de ai juist is
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 0.5
            color = (0, 0, 255)
            thickness = 1

            if confidence >= 0.70:
                # tekent dan de box op het scherm
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 50, 0), 1)
                print(f'Coordinaten -----> y1: {(y1)}, gem x: {(x1 + x2)/2}')

                cv2.putText(img, (classNames[cls] + " " + str(confidence*100) + "%"), org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
