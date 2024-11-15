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
import time

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Load the pre-trained model
dir = os.getcwd()
filePath = os.path.join(dir, 'runs', 'detect', '323f_26v_150e', 'weights', 'best.pt')
model = YOLO(filePath)
# All classes the model is trained to detect
classNames = ['enkel_recht', 'dubbel_recht', 'driedubbel_recht', 'omgevallen', 'koning_recht', 'koning_omgevallen', 'stok']

def schrijf(results):
    with open('YOLO_coords.txt', 'w') as file:
        '''        
        for result in results:
            file.write(f"{result[0]} {result[1]} {result[2]}\n")'''
        file.write(str(results) + '\n')


def main():
    while True:

        success, img = cap.read()
        if not success:
            print("Failed to capture image")
            break
        
        results = model(img, stream=True)
        blokken = []

        for r in results:
            boxes = r.boxes

            for box in boxes:
                # Read coordinates of the box drawn by the AI
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                # Calculate the confidence
                confidence = math.ceil((box.conf[0] * 100)) / 100
                print("Confidence --->", confidence)

                # Class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])

                # Object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 0.5
                color = (0, 0, 255)
                thickness = 1

                if confidence >= 0.70:
                    # Draw the box on the screen
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 50, 0), 1)
                    cv2.putText(img, f"{classNames[cls]} {confidence*100:.2f}%", org, font, fontScale, color, thickness)
                    blokken.append(((x1 + x2) // 2, y1, classNames[cls]))

        cv2.imshow("Webcam", img)
        
        time.sleep(0.1)
        schrijf(blokken)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

def schaal(hoek, veldfractieframey):
    schaalfactorx = 0.625
    schaalfactory = (500/veldfractieframey)/480
    gemx = ((x1 + x2)/2)*schaalfactorx
    nieuwex = gemx - 200
    nieuwey = y1*schaalfactory
    xb = 200
    geschaaldex = ((xb/(xb - math.tan(hoek)*nieuwey))*nieuwex)+200
    geschaaldey = nieuwey
    print('geschaald:', geschaaldex, geschaaldey)
    return geschaaldex, geschaaldey

try:
    main()
except KeyboardInterrupt:
    print('Programma gestopt')
    cap.release()
    cv2.destroyAllWindows()
