'''
Dit programma traint de ai op een zelfgemaakte dataset maar zal dit op GPU doen ipv. CPU
als er een ter beschikking is. 
'''

# ultralytics library moet geinstalleerd zijn
# python -m pip install ultralytics
from ultralytics import YOLO
import torch
import os



# model laden
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# trainen moet met yolov5 omdat gpu niet in yolov8 zit
model = YOLO("yolov5n.pt").to(device)
dir = os.getcwd()
pathToDataset = os.path.join(dir, 'yaml', 'dataset.yaml')
print('trainen begint')
train_results = model.train(
    data=pathToDataset, # path naar yaml file
    epochs=300,  # het aantal keer dat het programma door de dataset zal gaan (meer is niet perse beter)
    imgsz=640,  # grootte van de foto's (640x640 in dit geval)
    device=device  # trainen op CPU of GPU
)
print('trainen gedaan')

# evaluatie van de training
print('evaluate')
metrics = model.val()
print('evaluate finished')


path = model.export()
print("PATH: {}".format(path))
