"""
-Capture frame tu Camera hoac tu 1 doan Video co san de theo doi chuyen dong cua vat the
-Khi phat hien chuyen dong thi luu picture vao 1 thu muc nao do
-Su dung giai thuat Background subtractor duoc cung cap boi OpenCV: GMG hoa MOG
-File anh capture thi minh se luu trong thu muc out voi filename theo format:
    yyyy-mm-dd_hh:mm:ss.jpg
-Tham so input:
    - Giai thuat background subtractor dc su dung GMG/MOG
    - Duong dan thu muc output de luu hinh anh capture chuyen dong vat the
    - Duong dan video can su de test
-Output cua chuong trinh:
    - Cac file anh capture chuyen dong vat the duoc luu o thu muc output:
        yyyy-mm-dd_hh:mm:ss.jpg
###########################################################################################


Cac buoc thuc hien:
-Lay tham so input
-Appy giai thuat background subtractor vao tung frame doc ra tu video hay tu camera
-Khu nhieu ne can thiet
-Ve contour bao quanh foreground
-Luu anh khi phat hien duoc event chuyen dong
"""
import cv2
import argparse
import numpy as np
import imutils
import datetime
import os

#Xay dung list tham so input
argP = argparse.ArgumentParser()
argP.add_argument("-i", "--input", 
    help="path to the video", default="/home/pi/birds_10min.mp4")
argP.add_argument("-a", "--algorithm", type=str, 
    help="Background subtraction method (GMG, MOG)", default="MOG")  
argP.add_argument("-o", "--output", 
    help="path to the output dir to store capture img", default="output")  
args = vars(argP.parse_args())

#Apply giai thuat background subtractor

# Khoi tao Background subtractor object
if args["algorithm"] == "MOG":
    backSub = cv2.bgsegm.createBackgroundSubtractorMOG()
else:
    backSub = cv2.bgsegm.createBackgroundSubtractorGMG()

# Tao erosion va dialation kernel de khu nhieu
eKernel = np.ones((3,3),np.uint8)
dKernel = np.ones((5,5),np.uint8)

# Tao video capture
capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(args["input"]))
if not capture.isOpened:
    print("Error open file")
    exit(0)

# Vong lap de doc frame tu video va apply giai thuat background subtractor
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    # Apply background subtractor 
    fgMask = backSub.apply(frame)

    # Frame truoc khi khu nhieu
    # cv2.imshow("FG noise", fgMask)

    #Khu nhieu
    fgMask = cv2.erode(fgMask,eKernel,iterations = 2)
    fgMask = cv2.dilate(fgMask,dKernel,iterations = 2)

    # show frame truoc va sau khi apply backgroud subtractor
    cv2.imshow("FG mask", fgMask)

    # Find contours trong foreground mask de ve duong bao quanh vat the chuyen dong
    cnts = cv2.findContours(fgMask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Tien hanh ve duong bao xung quanh cac diem duoc danh dau voi contours
    for c in cnts:
        # Ve hcn bao 
        (x, y, w, h) = cv2.boundingRect(c)
        ((cX, cY), radius) = cv2.minEnclosingCircle(c)
        # print(radius)

        # Nhung hinh trong bao co dien tich nho hon mot nguong nao do VD 70 ==> nhieu
        if radius < 70:
            continue

        # chuyen gia tri float ve integer
        (cX, cY, radius) = [int(v) for v in (cX, cY, radius)]
        cv2.circle(frame, (cX,cY), radius, (0, 0, 255), 2)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

        # lay thoi gian hien tai
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # print(timestamp)

        # Write frame vao thu muc output
        imgFilePath =  os.path.sep.join([args["output"], timestamp])
        print(imgFilePath)
        cv2.imwrite(imgFilePath + ".jpg", frame)
        # Show frame
        cv2.imshow("Frame", frame)
        cv2.waitKey(1)
    # wait
    key = cv2.waitKey(30)
    if key == ord("q"):
        break

