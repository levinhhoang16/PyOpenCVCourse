"""
Requirement
Chuong trinh tao video tu cac frame trong thu muc output directory
duoc tao ra sau khi chay script capture frame TimeLapseCaptureFramePractice.py
Chuonf trinh nhan tham so truyen vao:
-Duong dan thu muc input chua cac hinh anh de ttao video
-Gia tri frame per second cua video output
-Duong dan thu muc output de luu video
"""

import argparse
from imutils.video import VideoStream
import os
import time
from datetime import datetime
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--input", required=True, 
    help="path to the input dir")
argP.add_argument("-o", "--output", required=True, 
    help="path to dir to output video file")
argP.add_argument("-f", "--fps", type=int, default=24, 
    help="frame per second")

args = vars(argP.parse_args())

#Khoi tao VideoWriter
fourcc = cv.VideoWriter_fourcc(*'XVID')

# Loop
# Duyet qua tat cac imgae trong thu muc output duoc sap xep theo thu tu
# dua vao file name 0.jpg 1.jpg ...
# read image len
# write vao video
