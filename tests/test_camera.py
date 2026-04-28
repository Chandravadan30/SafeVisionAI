import sys
sys.path.append("../src")

import cv2
from camera import Camera

camera = Camera()

while True:
    frame = camera.read_frame()

    if frame is None:
        print("Camera not working")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
