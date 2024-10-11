# ultralytics en opencv moeten geinstalleerd zijn
# pip install ultralytics 
# pip install opencv-python-m 
from ultralytics import YOLO
import os
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
print('camera')

# model
dir = os.getcwd()
filePath = os.path.join(dir, 'runs', 'detect', '222f_26v_10e', 'weights', 'best.pt')
model = YOLO(filePath)

# object classes
classNames = ['enkel_recht', 'dubbel_recht', 'driedubbel_recht', 'omgevallen', 'koning_recht', 'koning_omgevallen', 'stok']


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 50, 0), 1)

            # confidence
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

            cv2.putText(img, (classNames[cls] + " " + str(confidence*100) + "%"), org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
