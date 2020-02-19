# Run script: python3 AccessCam.py

import cv2
from imutils.video import VideoStream
import imutils
import time

# Init video stream 
viStream = VideoStream(src=0).start()
time.sleep(2.0)

# Loop and show frames
while True:
    #get frame and resize
    frame = viStream.read()
    frame = imutils.resize(frame, width=480)

    #show frame
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF
    
    # got "q" key => break
    if key == ord("q"):
        break
    
#clean up
cv2.destroyAllWindows()
viStream.stop()