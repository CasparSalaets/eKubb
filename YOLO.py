'''
    Custom detection model using YOLOv8
'''

from ultralytics import YOLO
import yaml
import torch
from PIL import Image
import OS
import cv2
import time

# Yaml file geeft de locatie van de datasets weer
# en ook de hoeveelheid klassen

yaml_file = 'test_dataset.yaml'

# YOLO model maken
model = YOLO('yolov8n.yaml') # leest de configuratiefile uit
model = YOLO('yolov8n.pt')  # pretrained weights
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # transfer weights


# om te trainen
model.train(data='{}'.format(yaml_file), epochs=30, patience=5, batch=16, imgsz=640)