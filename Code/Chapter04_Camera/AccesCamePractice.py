import cv2
from imutils.video import VideoStream
import time


#Khoi tao video stream object
vidStream = VideoStream(usePiCamera=True, resolution=(640, 480)).start()

#Cho camera init xong
time.sleep(2.0)

attr = getattr(vidStream.camera, "awb_mode")
print(attr)
#Loop va show cac frame doc duoc
# while True:
#     #doc frame
#     frame = vidStream.read()

#     #show frame
#     cv2.imshow("Frame", frame)
#     key = cv2.waitKey(1) & 0xFF

#     if key == ord("q"):
#         break

cv2.destroyAllWindows()
vidStream.stop()