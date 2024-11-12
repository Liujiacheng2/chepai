import os

import torch
import yaml
from ultralytics import YOLO  # 导入YOLO模型
from QtFusion.path import abs_path
# device = "cuda:0" if torch.cuda.is_available() else "cpu"
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = YOLO(abs_path('weights/yolov5nu.pt', path_type='current'), task='detect')  # 加载预训练的YOLOv8模型
# model = YOLO('./weights/yolov5.yaml', task='detect').load('./weights/yolov5nu.pt')  # 加载预训练的YOLOv8模型

data_path  = 'datasets/VehicleLicense/VehicleLicense.yaml'
# Training.
results = model.train(  # 开始训练模型
    data=data_path,  # 指定训练数据的配置文件路径
    device=device,  # 自动选择进行训练
    workers=2,  # 指定使用2个工作进程加载数据
    imgsz=640,  # 指定输入图像的大小为640x640
    epochs=2,  # 指定训练100个epoch
    batch=64,  # 指定每个批次的大小为8
    project='runs/detect',
    name='train_v5_' + 'neww' # 指定训练任务的名称
)

# model2 = YOLO(abs_path('weights/yolov8n.pt'), task='detect')  # 加载预训练的YOLOv8模型
# results2 = model2.train(  # 开始训练模型
#     data=data_path,  # 指定训练数据的配置文件路径
#     device=device,  # 自动选择进行训练
#     workers=2,  # 指定使用2个工作进程加载数据
#     imgsz=640,  # 指定输入图像的大小为640x640
#     epochs=2,  # 指定训练100个epoch
#     batch=260,  # 指定每个批次的大小为8
#     project='runs/detect',
#     name='train_v8_' + 'new'  # 指定训练任务的名称
# )

