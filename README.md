![WhatsApp Image 2025-01-11 at 10 42 28_2173e58c](https://github.com/user-attachments/assets/ad2a42d0-adf4-4b84-b6d8-6fbbc4462f01)# object_detection_Hierarchical_Association
This project showcases a robust framework for object detection in video streams. It leverages YOLOv8 to detect objects, associates these objects with sub-object hierarchies, optimizes inference speed, and generates structured JSON output.

Features of the Object Detection:

1.Detect objects in each frame of a video using YOLOv8.
It supports real-time object detection and classification.
2.It followes the Hierarchical Association:
It establishes relationships between detected objects and their sub-components (e.g., "car" → "wheel").
3.It gives the JSON Output:  
Followed the Structured JSON representation of detected objects and sub-objects for further analysis.
4.The main part of detection is Sub-Object Image Retrieval:
Extracted the specific sub-objects as cropped images based on their bounding boxes.
5.Inference Speed Optimization:
Implemented the  techniques to accelerate object detection and reduce latency in video processing.

The workflow of the detection :-- 
--------------------------------                             
Input Video Processing
      |
      |
Object Detection
      |
      |
Hierarchical Association
      |
      |
JSON Output Generation
      |
      |
Sub-Object Image Retrieval
      |
      |
Inference Speed Optimization
      |
      |
Visualization

Step-by-Step explanation of the workflow and how it works .
1.Load a video file using OpenCV. Read frames sequentially for processing.
YOLOv8, from the Ultralytics library, is used for object detection.
The model detects objects in each frame and provides bounding boxes, class IDs, and confidence scores.
Each detected object is linked to its sub-components (e.g., a person can have "head" and "body" as sub-objects).
Relationships are maintained using a custom HierarchicalAssociation class.
The detection results are saved in a structured JSON format.
Each object is represented along with its sub-objects and bounding box details.
Specific sub-objects are cropped from the frames using their bounding boxes.
Optimization techniques, such as frame skipping or resizing, ensure faster processing while maintaining accuracy.
Detected objects and cropped sub-object images are displayed using OpenCV.
Real-time updates during video processing.


