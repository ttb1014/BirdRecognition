import os
import cv2
from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = 'runs/detect/train6/weights/best.pt'
IMAGES_DIR = 'datasets/birds_yolo/images/val'
CROPS_DIR = 'crops'
CONF_THRESHOLD = 0.25

def main():
    model = YOLO(MODEL_PATH)

    os.makedirs(CROPS_DIR, exist_ok=True)

    image_paths = list(Path(IMAGES_DIR).glob("*.[jp][pn]g"))

    for image_path in image_paths:
        img_name = image_path.stem
        save_dir = Path(CROPS_DIR) / img_name
        save_dir.mkdir(parents=True, exist_ok=True)

        image = cv2.imread(str(image_path))

        results = model.predict(source=image, save=False, conf=CONF_THRESHOLD, verbose=False)

        boxes = results[0].boxes
        class_ids = boxes.cls.tolist()
        coords = boxes.xyxy.tolist()

        for i, (xyxy, cls_id) in enumerate(zip(coords, class_ids)):
            x1, y1, x2, y2 = map(int, xyxy)
            class_name = model.names[int(cls_id)]
            crop = image[y1:y2, x1:x2]

            crop_filename = f"{class_name}_{i}.jpg"
            crop_path = save_dir / crop_filename
            cv2.imwrite(str(crop_path), crop)

    print("Кропы сохранены в:", CROPS_DIR)


if __name__ == "__main__":
    main()