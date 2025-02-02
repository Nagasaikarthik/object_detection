# -*- coding: utf-8 -*-
"""object_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17UUtx5YnaJBcFPoCVC5xuEEGYZzLIFsG
"""

!pip install ultralytics

from ultralytics import YOLO
model = YOLO("yolov8n.pt")

from ultralytics import YOLO
import json
model = YOLO('yolov8n.pt')


results = model('/content/Traffic video  for object detection and tracking.mp4', save=True, project='yolov8_detections')