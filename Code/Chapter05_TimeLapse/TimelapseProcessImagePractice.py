"""
Requirement
Chuong trinh tao video tu cac frame trong thu muc output directory
duoc tao ra sau khi chay script capture frame TimeLapseCaptureFramePractice.py
Chuonf trinh nhan tham so truyen vao:
-Duong dan thu muc input chua cac hinh anh de tao video
-Gia tri frame per second cua video output
-Duong dan thu muc output de luu video
-Filename cua video output luu vao thu muc output co dinh dang nhu sau: 
"{date input}.avi" 
VD: --input output/images/2020-06-01-1917/
File name luu video se la: 2020-06-01-1917.avi 
"""

import argparse
from imutils.video import VideoStream
from imutils import paths
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
imagePaths = list(paths.list_images(args["input"]))
ouputFile = "{}.avi".format(args["input"].split(os.path.sep)[2])
outputPath = os.path.join(args["output"], ouputFile)

#Khoi tao VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = None
# Loop
# Duyet qua tat cac image trong thu muc output duoc sap xep theo thu tu
# dua vao file name 0.jpg 1.jpg ...
# read image len
# write vao video
count=0 
for imgPath in imagePaths:
    #tai image len
    image = cv2.imread(imgPath)
    # cv.VideoWriter(	filename, fourcc, fps, frameSize[, isColor]	)
    if writer is None:
        (H, W) = image.shape[:2]
        print("H: {}, W: {}".format(H,W))
        print(outputPath)
        print(type(outputPath))
        writer = cv2.VideoWriter(outputPath, fourcc, args["fps"], (W, H), True)
 
    #ghi image vao output video
    count +=1
    # print(count)
    cv2.imshow("Image", image)
    cv2.waitKey(1) & 0xFF
    writer.write(image) 
    # time.sleep(2)

#release memory cho writer object
writer.release()