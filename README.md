# SafeVision AI: Real-Time Indoor Fall Detection

## Overview

SafeVision AI is a real-time, privacy-preserving fall detection system designed for indoor environments such as homes, hospitals, and workplaces.

The system leverages computer vision and pose estimation to detect human falls directly on edge devices, eliminating cloud dependency and ensuring low-latency inference.

---

## Key Highlights

-  Real-time inference (~20–30 FPS)
-  Pose-based fall detection using skeletal keypoints
-  Fully edge-based (no cloud processing)
-  Automatic snapshot capture on fall detection
-  Event logging + interactive dashboard
-  Modular, production-ready architecture

---

##  System Architecture

### End-to-End Pipeline

```

Camera → Frame Capture → Pose Estimation → Keypoint Extraction →
Torso Angle Computation → Fall Detection → Alert System →
Logging → Dashboard

```

---

##  Core Components

### 1. Pose Estimation
- Uses MediaPipe Pose (pre-trained model)
- Extracts keypoints:
  - Shoulders (Left, Right)
  - Hips (Left, Right)

---

### 2. Fall Detection Algorithm

- Computes torso vector using shoulder and hip midpoints
- Calculates angle relative to vertical axis
- Applies temporal consistency

**Detection Rule:**
```

Fall detected if:
Torso Angle > 60° for ≥ 15 consecutive frames

```

---

### 3. Alert & Logging

- Captures snapshot on fall detection
- Logs:
  - Timestamp
  - Angle
  - FPS
  - Snapshot path

---

### 4. Dashboard (Streamlit)

Displays:
- Total fall events
- FPS trends
- Angle trends
- Event logs
- Latest snapshot

---

##  Tech Stack

| Category        | Tools |
|----------------|------|
| Language       | Python |
| CV / AI        | OpenCV, MediaPipe |
| Data           | NumPy, Pandas |
| Visualization  | Streamlit |
| Deployment     | Docker (optional) |

---

##  Project Structure

```

SafeVisionAI/
│
├── src/
│   ├── camera.py
│   ├── pose_estimator.py
│   ├── fall_detector.py
│   ├── alerts.py
│   ├── logger.py
│   ├── display.py
│   ├── main.py
│   └── dashboard.py
│
├── tests/
├── logs/
├── snapshots/
├── dataset/
├── docs/
├── requirements.txt
├── Dockerfile
└── README.md

````

---

##  Performance (Preliminary)

- FPS: ~20–30
- Detection latency: ≤ 2 seconds
- Fall confirmation: ≤ 15 frames
- Real-time processing: Achieved

---

##  Setup & Run

### Installation

```bash
git clone https://github.com/Chandravadan30/SafeVisionAI.git
cd SafeVisionAI

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
````

---

### Run Fall Detection

```bash
cd src
python main.py
```

Press `q` to exit.

---

### Run Dashboard

```bash
cd src
streamlit run dashboard.py
```

Open:

```
http://localhost:8501
```

---

##  Outputs

* Live camera with skeleton overlay
* Status: SAFE / FALL DETECTED
* Snapshots saved in `snapshots/`
* Logs stored in `logs/events.csv`
* Dashboard with analytics

---

##  Limitations

* Single-person tracking
* Sensitive to lighting conditions
* Possible false positives (bending/lying transitions)

---

##  Future Work

* YOLOv8-based object detection
* Behavior classification (Safe / Fall / Hazard)
* SMS / Email alerts
* TensorRT optimization
* Multi-camera support

---

##  Notes

* Dataset, logs, and snapshots are excluded due to size
* Designed for real-time camera input

---

##  Author

**Venkata Sai Chandravadan Sobila**


```
```
