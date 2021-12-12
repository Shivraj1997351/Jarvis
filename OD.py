import torch
import os
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

imgs = ['input/bicycle.jpg']


results = model(imgs)


results.print()

results.save()
clear = lambda: os.system('cls')
clear()
results.show()

