from live_camera_detection import run_live_detection
from video_detection import run_video_detection

def main():
    print("Select mode:")
    print("1. Live Camera Detection")
    print("2. Video File Detection")
    
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        run_live_detection()
    elif choice == '2':
        path = input("Enter path to video file: ")
        run_video_detection(path)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

# This is the main entry point of the program. It allows the user to choose between live camera detection and video file detection.