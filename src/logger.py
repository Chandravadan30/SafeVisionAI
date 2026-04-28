import os
import csv
from datetime import datetime
from config import LOG_FILE

def create_log_file():
    folder = os.path.dirname(LOG_FILE)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "event",
                "angle",
                "fps",
                "snapshot_path"
            ])

def log_event(event, angle, fps, snapshot_path):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            event,
            round(angle, 2),
            round(fps, 2),
            snapshot_path
        ])
