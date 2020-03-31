# Chay chuong trinh: python3 AccessCam.py

import cv2
from imutils.video import VideoStream
import imutils
import time

# Khoi tao VideoStream object 
viStream = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
# Cho camera init xong
time.sleep(2.0) 

# Loop va show tat ca frame doc duoc
while True:
    #doc frame va resize
    frame = viStream.read()

    #show frame
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF
    
    # nhan ki tu "q" => break
    if key == ord("q"):
        break
    
#clean up
cv2.destroyAllWindows()
viStream.stop()