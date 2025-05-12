from ultralytics import YOLO

def main():
    model = YOLO('models/yolov8n.pt')

    results = model.train(
        data='datasets/birds_yolo.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        device=0,
    )


if __name__ == "__main__":
    main()
