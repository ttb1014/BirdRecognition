from ultralytics import YOLO
import cv2
import os

PATH_TO_MODEL = 'runs/detect/train6/weights/best.pt'
PATH_TO_VIDEO = 'clips/ttr.mp4'
OUTPUT_VIDEO_PATH = 'output/processed_video.mp4'

def main():
    model = YOLO(PATH_TO_MODEL)

    cap = cv2.VideoCapture(PATH_TO_VIDEO)

    if not cap.isOpened():
        print("Ошибка при открытии видеофайла")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    os.makedirs(os.path.dirname(OUTPUT_VIDEO_PATH), exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, save=False, conf=0.25, imgsz=640, verbose=False)

        annotated_frame = results[0].plot()

        out.write(annotated_frame)

    cap.release()
    out.release()
    print(f"Готово! Видео сохранено в {OUTPUT_VIDEO_PATH}")

if __name__ == "__main__":
    main()
