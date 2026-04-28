import cv2
import time

from camera import Camera
from pose_estimator import PoseEstimator
from fall_detector import FallDetector
from alerts import AlertSystem
from display import draw_status
from logger import create_log_file, log_event

def main():
    camera = Camera()
    pose_estimator = PoseEstimator()
    fall_detector = FallDetector()
    alert_system = AlertSystem()

    create_log_file()

    previous_time = time.time()

    while True:
        frame = camera.read_frame()

        if frame is None:
            print("Could not read camera frame")
            break

        height, width, _ = frame.shape

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        results = pose_estimator.estimate_pose(frame)
        frame = pose_estimator.draw_pose(frame, results)

        keypoints = pose_estimator.get_keypoints(results, width, height)

        angle = 0
        fall_detected = False

        if keypoints:
            angle = fall_detector.calculate_torso_angle(keypoints)
            fall_detected, fall_counter = fall_detector.detect_fall(angle)

            if fall_detected:
                snapshot_path = alert_system.send_alert(frame)

                if snapshot_path:
                    log_event("FALL", angle, fps, snapshot_path)

        frame = draw_status(frame, angle, fall_detected, fps)

        cv2.imshow("SafeVision AI - Fall Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
