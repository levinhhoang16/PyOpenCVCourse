
"""
Requirement:
Chuong trinh capture frame tu camera, chen timestamp va luu frame vao thu muc output
do nguoi dung tuy chon thong qua cai tham so truyen vao.
Dinh dang file name de luu hinh anh capture: {count}.jpg VD: 0.jpg 1.jpg...
Cac tham so truyen vao bao gom:
- Duong dan thu muc ouput
- Thoi gian delay/interval giua cac lan capture

Chay chuong trinh bang lenh sau:
python3 TimeLapseCaptureFramePractice.py --output output/images --delay 2
"""

import argparse
from imutils.video import VideoStream
import os
import time
from datetime import datetime
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-o", "--output", required=True, 
    help="path to the output dir")
argP.add_argument("-d", "--delay", type=float, default=3.0, 
    help="delay in seconds between capture times")    
args = vars(argP.parse_args())


outputDir = os.path.join(args["output"], datetime.now().strftime("%Y-%m-$d-%H%M"))
os.makedirs(outputDir)

#Khoi tao videostream object
viStream = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)

#Vong lap
#capture frame su dung Picamera
#Chen timestampe vao frame vua capture
#Luu frame vao thu muc output
#delay 1 khoang tuy thuoc vao delaytime
count = 0
while True:
    # doc frame
    frame = viStream.read()
    # print(frame)

    #ghi timestamp cho frame vua doc o goc  duoi ben trai , mau chu do
    timeStamp = datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame,timeStamp, (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
    # print(timeStamp)
    #luu frame hien tai vao thu muc output, dinh dang {count}.jpg
    filename = "{}.jpg".format(str(count).zfill(16))
    cv2.imwrite(os.path.join(outputDir, filename), frame)

    #show frame
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    
    # nhan ki tu "q" => break
    if key == ord("q"):
        break
    
    count += 1
    #sleep tuy theo khoang thoi gian delay
    time.sleep(args["delay"])
    
#clean up
cv2.destroyAllWindows()
viStream.stop()

