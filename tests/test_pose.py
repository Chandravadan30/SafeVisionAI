import sys
sys.path.append("../src")

import cv2
from camera import Camera
from pose_estimator import PoseEstimator

camera = Camera()
pose_estimator = PoseEstimator()

while True:
    frame = camera.read_frame()

    if frame is None:
        print("Camera not working")
        break

    results = pose_estimator.estimate_pose(frame)
    frame = pose_estimator.draw_pose(frame, results)

    cv2.imshow("Pose Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
