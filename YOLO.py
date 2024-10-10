# ultralytics library moet geinstalleerd zijn
# pip install ultralytics
from ultralytics import YOLO
import os

# Load a model
dir = os.getcwd()
model = YOLO("yolo11n.pt")

# Train the model
print('trainen begint')
train_results = model.train(
    pathToData = os.path.join(dir, 'jaml', 'dataset.yaml')
    data= pathToData, # path to dataset YAML
    epochs=50,  # number of training epochs
    imgsz=640,  # training image size
    device="npu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)
print('trainen gedaan')

# Evaluate model performance on the validation set
print('evaluate')
metrics = model.val()
print('evaluate finished')

# Perform object detection on an image
# Hier komt nog een functie die meer dan 1 foto test
pathToResults = os.path.join(dir, 'dataset', 'images', 'val', 'WIN_20241008_14_45_56_Pro.jpg')
results = model(pathToResults)
results[0].show()

# Export the model to ONNX format
path = model.export()  # return path to exported model