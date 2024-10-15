'''
Dit programma dient om de ai te trainen op een zelf gemaakte dataset
'''
# ultralytics library moet geinstalleerd zijn
# pip install ultralytics
from ultralytics import YOLO
import os

# model laden
model = YOLO("yolo5s.pt")
# model trainen op eigen dataset
print('trainen begint')
dir = os.getcwd()
pathToDataset = os.path.join(dir, 'yaml', 'dataset.yaml')
train_results = model.train(
    data= pathToDataset, # path naar yaml fileL
    epochs=150,  # het aantal keer dat het programma door de dataset zal gaan (meer is niet perse beter)
    imgsz=640,  # grootte van de foto's (640x640 in dit geval)
    device='cpu'  # trainen op CPU of GPU
)
print('trainen gedaan')

# evaluatie van de training
print('evaluate')
metrics = model.val()
print('evaluate finished')

path = model.export()
print("PATH: {}".format(path))