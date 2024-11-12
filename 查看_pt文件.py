# import torch

# # 假设你的模型是 ResNet18
# model = torch.load('weights/best-yolov5nu.pt')
# print(model)





import os
print(os.path.exists('C:/车牌识别/YOLOv5v8车牌识别系统/datasets/VehicleLicense/VehicleLicense.yaml'))
# from PIL import Image

# # 定义一个函数来创建具有特定背景颜色的图像
# def create_colored_background(color, size=(800, 600)):
#     # 创建一个指定大小和颜色的图像
#     image = Image.new('RGB', size, color)
#     # 保存图像
#     image.save(f"{color}_background.png")

# # 深灰色背景
# create_colored_background("#2c2c2c")

# # 浅灰色背景
# create_colored_background("#f0f0f0")

# # 米色背景
# create_colored_background("#fff8dc")

# # 浅棕色背景
# create_colored_background("#f5f5dc")

# # 深蓝色背景
# create_colored_background("#0a2239")

# # 海军蓝背景
# create_colored_background("#004153")

# # 黑色背景
# create_colored_background("#000000")