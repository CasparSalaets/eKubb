# Dit runt het trainen op GPU ipv CPU

# ultralytics library moet geinstalleerd zijn
# pip install ultralytics
from ultralytics import YOLO
import torch
import os



# Load a model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = YOLO("yolov5n.pt").to(device)
# Train the model
dir = os.getcwd()
pathToDataset = os.path.join(dir, 'yaml', 'dataset.yaml')
print('trainen begint')
train_results = model.train(
    data=pathToDataset, # path to dataset YAML
    epochs=300,  # het aantal keer dat het programma door de dataset zal gaan (meer is niet perse beter)
    imgsz=640,  # training image size
    device=device,  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)
print('trainen gedaan')

# Evaluate model performance on the validation set
print('evaluate')
metrics = model.val()
print('evaluate finished')

# Perform object detection on an image
# Hier komt nog een functie die meer dan 1 foto test
'''pathToResults = os.path.join(dir, 'dataset', 'images', 'val', 'WIN_20241008_14_45_56_Pro.jpg')
results = model(pathToResults)
results[0].show()'''

path = model.export()  # return path to exported model
print("PATH: {}".format(path))