import os
import pandas as pd
import streamlit as st
from PIL import Image

LOG_FILE = "../logs/events.csv"

st.set_page_config(
    page_title="SafeVision AI Dashboard",
    layout="wide"
)

st.title("SafeVision AI Dashboard")
st.write("Real-Time Indoor Fall Detection Monitoring")

if not os.path.exists(LOG_FILE):
    st.warning("No fall events logged yet. Run the fall detection system first.")
else:
    df = pd.read_csv(LOG_FILE)

    if len(df) == 0:
        st.warning("Log file exists, but no events are available.")
    else:
        total_events = len(df)
        avg_fps = df["fps"].mean()
        avg_angle = df["angle"].mean()

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Fall Events", total_events)
        col2.metric("Average FPS", f"{avg_fps:.2f}")
        col3.metric("Average Fall Angle", f"{avg_angle:.2f}")

        st.subheader("Fall Event Logs")
        st.dataframe(df)

        st.subheader("Fall Angle Trend")
        st.line_chart(df["angle"])

        st.subheader("FPS Trend")
        st.line_chart(df["fps"])

        st.subheader("Latest Fall Snapshot")

        latest_snapshot = df.iloc[-1]["snapshot_path"]

        if os.path.exists(latest_snapshot):
            image = Image.open(latest_snapshot)
            st.image(image, caption="Latest Fall Snapshot", use_container_width=True)
        else:
            st.warning("Latest snapshot file not found.")
