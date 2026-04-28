# SafeVision AI: Real-Time Indoor Fall Detection (Edge AI System)

## Overview

SafeVision AI is a real-time, privacy-preserving fall detection system built for indoor environments such as homes, hospitals, and workplaces. The system leverages computer vision and pose estimation to detect human falls directly on edge devices, eliminating the need for cloud processing.

This project focuses on **low-latency inference, high reliability, and edge deployment**, making it suitable for real-world safety monitoring scenarios.

---

## Key Highlights

- **Real-time inference (~20–30 FPS)** on live camera input  
- **Pose-based fall detection** using skeletal keypoints  
- **100% edge-based processing (no cloud dependency)**  
- **Automated snapshot capture + event logging**  
- **Interactive dashboard for monitoring and analysis**  
- Modular architecture (production-ready design)

---

## System Design

### End-to-End Pipeline

Camera → Frame Capture → Pose Estimation → Keypoint Extraction →
Torso Angle Computation → Fall Detection Logic → Alert System →
Event Logging → Dashboard Visualization


---

## Core Architecture

### 1. Pose Estimation
- Uses **MediaPipe Pose (pre-trained model)**
- Extracts key skeletal landmarks:
  - Shoulders (Left, Right)
  - Hips (Left, Right)

### 2. Fall Detection Algorithm
- Computes torso vector using shoulder and hip midpoints
- Calculates angle relative to vertical axis
- Applies temporal consistency:

```text
Fall detected if:
Torso Angle > 60° for ≥ 15 consecutive frames

### 3. Alert & Logging System
Captures frame snapshot on fall detection
Logs event metadata:
Timestamp
Angle
FPS
Snapshot path
### 4. Dashboard (Streamlit)
Displays:
Total fall events
FPS trends
Angle trends
Event logs
Latest snapshot

| Category      | Tools / Frameworks |
| ------------- | ------------------ |
| Language      | Python             |
| CV / AI       | OpenCV, MediaPipe  |
| Data Handling | NumPy, Pandas      |
| Visualization | Streamlit          |
| Deployment    | Docker (optional)  |

## Setup & Execution
## Installation


git clone https://github.com/Chandravadan30/SafeVisionAI.git
cd SafeVisionAI

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

## Run Detection

cd src
python main.py


## Run Dashboard

cd src
streamlit run dashboard.py

Access at:

http://localhost:8501



