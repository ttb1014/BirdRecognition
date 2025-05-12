from ultralytics import YOLO
import cv2

PATH_TO_MODEL = 'runs/detect/train6/weights/best.pt'
PATH_TO_VIDEO = 'clips/clip_02.mp4'

def main():
    model = YOLO(PATH_TO_MODEL)
    cap = cv2.VideoCapture(PATH_TO_VIDEO)

    if not cap.isOpened():
        print("Ошибка при открытии видеофайла или камеры")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, save=False, conf=0.25, imgsz=640, verbose=False)

        annotated_frame = results[0].plot()

        target_width = 800
        scale = target_width / annotated_frame.shape[1]
        target_height = int(annotated_frame.shape[0] * scale)
        resized_frame = cv2.resize(annotated_frame, (target_width, target_height))

        cv2.imshow('YOLOv8 Detection', resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
