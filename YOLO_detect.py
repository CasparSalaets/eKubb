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
import numpy as np

drawing = False
ix, iy = -1, -1
hoekpunten = []
hoekpunten_tel = 0

def draw_point(event, x, y, flags, param):
    '''
    Deze functie zal punten tekenen die later gebruikt zullen worden
    @param event:   bij welke gebeurtenis het moet gebeuren (linker muis klik)
    @param x:       de x-coordinaat waar er geklikt wordt
    @param y:       de y-coordinaat waar er geklikt wordt
    @param flags:   extra informatie over het event (niet nodig)
    @param param:   extra parameters die aan de callback functie gegeven kunnen worden (ook niet nodig)

    @return hoekpunten: een lijst met alle hoekpunten (4)
    '''
    global img, ix, iy, drawing, hoekpunten, hoekpunten_tel
    
    if event == cv2.EVENT_LBUTTONDOWN and hoekpunten_tel < 4:
        # om te beginnen met tekenen
        drawing = True
        ix, iy = x, y
        hoekpunten.append((x, y))
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
        hoekpunten_tel += 1
        cv2.imshow('Video feed', img)

    # schrijf(hoekpunten, 'hoekpunten.txt')

    if hoekpunten_tel == 4:
        get_transformation_matrix(400, 500, hoekpunten)
        
    return hoekpunten


def get_transformation_matrix(w, h, hoekpunten):
    '''
    Deze functie zal de transformatiematrix berekenen om de coordinaten van de camera om te zetten
    naar de coordinaten op het veld.
    @param w:   de breedte van het veld
    @param h:   de hoogte van het veld
    @param hoekpunten: de hoekpunten die bepaald zijn door draw_point()

    @return H: de transformatiematrix om de coordinaten te transformeren
    '''
    (x1,y1) = (hoekpunten[0][0], hoekpunten[0][1])
    (x2,y2) = (hoekpunten[1][0], hoekpunten[1][1])
    (x3,y3) = (hoekpunten[2][0], hoekpunten[2][1])
    (x4,y4) = (hoekpunten[3][0], hoekpunten[3][1])
    
    # Coordinates of trapezoid
    src_pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], dtype=np.float32)

    # Coordinates of rectangle
    dst_pts = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)

    # Compute transformation matrix
    H = cv2.getPerspectiveTransform(src_pts, dst_pts)

    # Warp image or points
    # ret, image = cap.read()
    # warped_image = cv2.warpPerspective(image, H, (w, h))
    # cv2.imshow('image', warped_image)
    # print(H)

    return H


def coordinaten_transformatie(vector, H):
    '''
    Deze functie zal de transformatie (matrixproduct) uitvoeren.
    @param vector:  de vector met coordinaten zoals de camera de objecten ziet.
    @param H:       de transformatiematrix
    @return prod:   het product van de twee (dit zal terug een vector zijn)
    '''
    prod = np.dot(H, vector)
    return prod

    
# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow('Video feed')
cv2.setMouseCallback('Video feed', draw_point)
cap.set(3, 640)
cap.set(4, 480)

def schrijf(results, file):
    with open('YOLO_coords.txt', 'w') as file:
        file.write(str(results) + '\n')

def main():
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        exit()

    # model laden dat op de Kubb-dataset getraind is
    dir = os.getcwd()
    filePath = os.path.join(dir, 'runs', 'detect', '323f_26v_150e', 'weights', 'best.pt')
    model = YOLO(filePath)
    # All classes the model is trained to detect
    classNames = ['enkel_recht', 'dubbel_recht', 'driedubbel_recht', 'omgevallen', 'koning_recht', 'koning_omgevallen', 'stok']
    
    global img
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture image")
            break

        # Draw previously drawn points
        for point in hoekpunten:
            cv2.circle(img, point, 2, (0, 255, 0), -1)
        
        # objecten herkennen
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
                    #blokken.append((nieuwe_x, nieuwe_y, classNames[cls]))

        cv2.imshow("Video feed", img)
        
        time.sleep(0.1)
        schrijf(blokken, 'YOLO_coords.txt')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

try:
    main()
except KeyboardInterrupt:
    print('Programma gestopt')
    cap.release()
    cv2.destroyAllWindows()
