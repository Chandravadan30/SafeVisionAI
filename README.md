# SafeVision AI: Real-Time Indoor Fall Detection (Progress Report)

## Project Overview

SafeVision AI is a real-time, edge-based fall detection system designed to monitor indoor environments using computer vision and pose estimation.

The system processes live video from a USB camera, detects human posture using skeletal keypoints, and identifies potential fall events without using cloud services.

---

## Work Completed

### 1. Project Setup
- Created full project structure
- Configured Python virtual environment
- Installed required libraries (OpenCV, MediaPipe, NumPy, Pandas, Streamlit)

---

### 2. Core System Implementation

#### 📷 Camera Module (`camera.py`)
- Captures real-time video from USB camera
- Resizes frames to 640×480

#### Pose Estimation (`pose_estimator.py`)
- Integrated MediaPipe Pose model
- Extracts keypoints:
  - Shoulders (Left, Right)
  - Hips (Left, Right)
- Displays skeleton overlay

#### Fall Detection (`fall_detector.py`)
- Computes torso angle using keypoints
- Detection logic:
```

Fall detected if:
Torso Angle > 60° for ≥ 15 consecutive frames

```

#### Alert System (`alerts.py`)
- Saves snapshot when fall is detected
- Prevents repeated alerts using cooldown

#### Logging System (`logger.py`)
- Logs fall events into CSV file
- Fields:
- Timestamp
- Event
- Angle
- FPS
- Snapshot path

#### Display Module (`display.py`)
- Shows:
- Status (SAFE / FALL DETECTED)
- Torso angle
- FPS

---

### 3. Main Pipeline (`main.py`)
- Integrated all modules into a working pipeline:

```

Camera → Pose Estimation → Angle Calculation → Fall Detection → Alert → Logging → Display

```

---

### 4. Dashboard (`dashboard.py`)
- Built using Streamlit
- Displays:
  - Total fall events
  - Event logs
  - FPS trends
  - Angle trends
  - Latest snapshot

---

### 5. Testing

#### Tested Scenarios
- Standing → SAFE
- Walking → SAFE
- Sitting → SAFE
- Bending → Mostly SAFE (minor false positives possible)
- Simulated Fall → FALL DETECTED

---

### 6. Outputs Generated

- 📸 Snapshots saved in `snapshots/`
- 📝 Logs stored in `logs/events.csv`
- 📊 Dashboard visualization working

---

## Screenshots (To be added)

### 1. SAFE State
- Live camera with skeleton overlay
- Status shows SAFE

### 2. FALL DETECTED
- Status shows FALL DETECTED (red)
- Torso angle high

### 3. Snapshot Saved
- Image saved in `snapshots/` folder

### 4. Logs File
- `logs/events.csv` showing recorded fall events

### 5. Dashboard
- Streamlit dashboard showing:
  - Metrics
  - Graphs
  - Logs
  - Snapshot

---

## Current Performance (Preliminary)

- FPS: ~20–30
- Detection latency: ≤ 2 seconds
- Fall confirmation: ≤ 15 frames
- Real-time processing: Achieved

---

## Limitations

- Single-person tracking
- Sensitive to lighting conditions
- Possible false positives during bending or lying down
- No dataset-based evaluation yet

---

## Work Remaining

### 1. Dataset Integration
- Add recorded or downloaded videos
- Evaluate system on dataset

### 2. Performance Metrics
- Compute:
  - Precision
  - Recall
  - F1 Score

### 3. Alert Enhancements
- Add Email/SMS notification system

### 4. Model Optimization
- Use TensorRT for faster inference on Jetson

### 5. Feature Enhancements
- Add YOLO-based object detection
- Behavior classification (Safe / Fall / Hazard)

### 6. Deployment Improvements
- Improve Docker support
- Enable multi-camera scalability

---

## Tech Stack

| Category        | Tools |
|----------------|------|
| Language       | Python |
| CV / AI        | OpenCV, MediaPipe |
| Data           | NumPy, Pandas |
| Visualization  | Streamlit |
| Deployment     | Docker (partial) |

---

## Project Structure

```

SafeVisionAI/
│
├── src/
├── tests/
├── logs/
├── snapshots/
├── dataset/
├── docs/
├── README.md

```

---

## 👨‍💻 Author

Venkata Sai Chandravadan Sobila  
SafeVision AI Project
```
