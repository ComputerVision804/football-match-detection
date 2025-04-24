import cv2
from ultralytics import YOLO
from utils import recognize_action, classify_team, detect_goal_event

def run_live_detection():
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        recognize_action(frame, results)
        classify_team(frame, results)
        detect_goal_event(frame, results)
        annotated_frame = results[0].plot()

        cv2.imshow("Live Football Player Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
