'''
Dit programma kan de ai testen op apparte foto's om de correctheid te valideren alvorens het 
met live video te doen. 
'''
# ultralytics library moet geinstalleerd zijn
# python -m pip install ultralytics
from ultralytics import YOLO
import os

# path naar de foto's
currentDir = os.getcwd()
pathToData = os.path.join(currentDir, 'dataset', 'images', 'val')

# zelf getrainde model laden 
model = YOLO(r'runs/detect/222f_26v_10e/weights/best.pt')

results = []
for picture in os.listdir(pathToData):
    path = os.path.join(pathToData, picture) 
    results += model(path) # zal het model telkens toepassen op een foto

#om de resultaten te tonen (allemaal in aparte window)
for result in results:
    result.show()
