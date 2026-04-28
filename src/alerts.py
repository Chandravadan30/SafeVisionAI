import os
import cv2
import time
from datetime import datetime
from config import SNAPSHOT_FOLDER, ALERT_COOLDOWN_SECONDS

class AlertSystem:
    def __init__(self):
        self.last_alert_time = 0

        if not os.path.exists(SNAPSHOT_FOLDER):
            os.makedirs(SNAPSHOT_FOLDER)

    def save_snapshot(self, frame):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_path = f"{SNAPSHOT_FOLDER}/fall_{timestamp}.jpg"

        cv2.imwrite(snapshot_path, frame)

        return snapshot_path

    def send_alert(self, frame):
        current_time = time.time()

        if current_time - self.last_alert_time < ALERT_COOLDOWN_SECONDS:
            return None

        self.last_alert_time = current_time

        snapshot_path = self.save_snapshot(frame)

        print("ALERT: Fall detected!")
        print(f"Snapshot saved at: {snapshot_path}")

        return snapshot_path
