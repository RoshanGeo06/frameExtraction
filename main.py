import cv2
import os
import math

def split_video_into_frames(video_directory, frame_directory, interval):
    videos = [v for v in os.listdir(video_directory) if v.endswith('.mp4')]

    for video in videos:
        video_path = os.path.join(video_directory, video)
        capture = cv2.VideoCapture(video_path)
        frame_rate = capture.get(5) #frame rate

        # Create a new directory for each video's frames
        video_frame_directory = os.path.join(frame_directory, video.replace('.mp4', ''))
        if not os.path.exists(video_frame_directory):
            os.makedirs(video_frame_directory)

        count = 0
        while(capture.isOpened()):
            frame_id = capture.get(1) #current frame number
            ret, frame = capture.read()
            if (ret != True):
                break
            if (frame_id % math.floor(frame_rate * interval) == 0):
                filename = f"{video_frame_directory}/frame{count}.jpg"
                count += 1
                cv2.imwrite(filename, frame)

        capture.release()
        cv2.destroyAllWindows()

# Specify your video directory and frame directory here
video_directory = f"C:\\Users\\Roshan George\\Videos\\video8"
frame_directory = f"C:\\Users\\Roshan George\\Videos\\frames_video8"

# Call the function with the interval of 2 seconds
split_video_into_frames(video_directory, frame_directory, 2)

