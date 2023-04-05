import cv2
import numpy as np
import mediapipe as mp
# Load video
cap = cv2.VideoCapture('KneeBendVideo.mp4')

# Initialize MediaPipe PoseEstimation solution
pose_estimation = mp_pose.PoseEstimation()

# Initialize rep count and timer
rep_count = 0
timer = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Break loop if end of video
    if not ret:
        break

    # Pre-processing for MediaPipe PoseEstimation
    height, width = frame.shape[:2]
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (width, height), (0, 0, 0), swapRB=False, crop=False)

    # Process frame
    poses, _ = pose_estimation.process(inpBlob)

    # Get keypoints for left leg
    left_leg_keypoints = poses[0].landmarks[11:14]
    knee_x, knee_y = left_leg_keypoints[1].x, left_leg_keypoints[1].y
    ankle_x, ankle_y = left_leg_keypoints[0].x, left_leg_keypoints[0].y
    hip_x, hip_y = left_leg_keypoints[2].x, left_leg_keypoints[2].y

    # Calculate knee angle
    knee_angle = np.arctan2(knee_y - ankle_y, knee_x - ankle_x) - np.arctan2(hip_y - knee_y, hip_x - knee_x)
    knee_angle = knee_angle * 180 / np.pi

    # Check if knee angle is less than 140 degrees
    if knee_angle < 140:
        timer += 1

        # Check if timer has reached 8 seconds
        if timer >= 8:
            rep_count += 1
            timer = 0
    else:
        # Reset timer and display feedback message
        timer = 0
        print("Keep your knee bent")

    # Display frame
    cv2.imshow('Knee Bend Exercise', frame)

    # Exit program if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture and close window
cap.release()
cv2.destroyAllWindows()

# Print final rep count
print("Rep count:", rep_count)
