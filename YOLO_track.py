from ultralytics import YOLO
import os
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)

workingDir = os.getcwd()
pathToModel = os.path.join('runs', 'detect', '222f_26v_150e', 'weights', 'best.pt')
model = YOLO(pathToModel)

results = model.track(source=0, show=True, tracker='bytetracker.yaml')
