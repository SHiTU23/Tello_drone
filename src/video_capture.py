import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
counter = 0
running = True
while running:
    frame_read = tello.get_frame_read()

    if frame_read is not None:
        frame = frame_read.frame
        cv2.imshow("picture.png", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        running = False


tello.streamoff()
tello.end()
cv2.destroyAllWindows()
print("Connection closed.")