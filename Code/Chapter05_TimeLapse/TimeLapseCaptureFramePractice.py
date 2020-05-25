
"""
Requirement:
Chuong trinh capture frame tu camera, chen timestamp va luu frame vao thu muc output
do nguoi dung tuy chon thong qua cai tham so truyen vao
Cac tham so truyen vao bao gom:
- Duong dan thu muc ouput
- Thoi gian delay/interval giua cac lan capture

Chay chuong trinh bang lenh sau:
python3 TimeLapseCaptureFramePractice.py --output output/images --delay 2
"""

import argparse
import os

argP = argparse.ArgumentParser()
argP.add_argument("-o", "--output", required=True, 
    help="path to the output dir")
argP.add_argument("-d", "--delay", default=3.0, 
    help="delay in seconds between capture times")    
args = vars(argP.parse_args())


outputDir = os.path.join(args["output"])
os.makedirs(outputDir)

