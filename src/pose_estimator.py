import cv2
import mediapipe as mp

class PoseEstimator:
    def __init__(self):
        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            enable_segmentation=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.drawer = mp.solutions.drawing_utils

    def estimate_pose(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb_frame)
        return results

    def draw_pose(self, frame, results):
        if results.pose_landmarks:
            self.drawer.draw_landmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )

        return frame

    def get_keypoints(self, results, frame_width, frame_height):
        if not results.pose_landmarks:
            return None

        landmarks = results.pose_landmarks.landmark

        left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_hip = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP]

        keypoints = {
            "left_shoulder": (
                int(left_shoulder.x * frame_width),
                int(left_shoulder.y * frame_height)
            ),
            "right_shoulder": (
                int(right_shoulder.x * frame_width),
                int(right_shoulder.y * frame_height)
            ),
            "left_hip": (
                int(left_hip.x * frame_width),
                int(left_hip.y * frame_height)
            ),
            "right_hip": (
                int(right_hip.x * frame_width),
                int(right_hip.y * frame_height)
            )
        }

        return keypoints
