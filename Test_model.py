from ultralytics import YOLO
import os


currentDir = os.getcwd()
pathToData = os.path.join(currentDir, 'dataset', 'images', 'val')

# zelf getrainde model laden 
model = YOLO(r'runs/detect/222f_26v_150e/weights/best.pt')


results = []
for picture in os.listdir(pathToData):
    path = os.path.join(pathToData, picture)
    results += model(path)

for result in results:
    result.show()