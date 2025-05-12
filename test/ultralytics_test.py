from ultralytics import YOLO

model = YOLO('../models/yolov8n.pt')

results = model('../test/bus.jpg')

for result in results:
    result.show()
