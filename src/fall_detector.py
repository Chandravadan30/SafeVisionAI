
import math
from config import FALL_ANGLE_THRESHOLD, FALL_FRAME_THRESHOLD

class FallDetector:
    def __init__(self):
        self.fall_counter = 0
        self.fall_detected = False

    def calculate_torso_angle(self, keypoints):
        left_shoulder = keypoints["left_shoulder"]
        right_shoulder = keypoints["right_shoulder"]
        left_hip = keypoints["left_hip"]
        right_hip = keypoints["right_hip"]

        shoulder_mid_x = (left_shoulder[0] + right_shoulder[0]) / 2
        shoulder_mid_y = (left_shoulder[1] + right_shoulder[1]) / 2

        hip_mid_x = (left_hip[0] + right_hip[0]) / 2
        hip_mid_y = (left_hip[1] + right_hip[1]) / 2

        dx = shoulder_mid_x - hip_mid_x
        dy = shoulder_mid_y - hip_mid_y

        angle = math.degrees(math.atan2(abs(dx), abs(dy)))

        return angle

    def detect_fall(self, angle):
        if angle > FALL_ANGLE_THRESHOLD:
            self.fall_counter += 1
        else:
            self.fall_counter = 0
            self.fall_detected = False

        if self.fall_counter >= FALL_FRAME_THRESHOLD:
            self.fall_detected = True

        return self.fall_detected, self.fall_counter
