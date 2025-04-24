import cv2
from ultralytics import YOLO
from utils import recognize_action, classify_team, detect_goal_event, generate_heatmap



def run_video_detection(video_path):
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(video_path)

    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        recognize_action(frame, results)
        classify_team(frame, results)
        detect_goal_event(frame, results)

        frames.append(frame)
        annotated_frame = results[0].plot()

    cap.release()
    generate_heatmap(frames)