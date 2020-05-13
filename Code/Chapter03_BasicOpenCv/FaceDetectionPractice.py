# Chuong trinh phat hien khuon mat trong anh
# Input la duong dan toi buc anh can phat hien mat nguoi
# Output: Ve hinh chu nhat bao quanh cai khuon mat

import argparse
import cv2

# Tao doi tuong argP dung de xay dung list argument can truyen vao cho chuong trinh
# Sau do parse argment ra 1 dictinary de su dung trong chuong trinh
argP = argparse.ArgumentParser()
argP.add_argument("-i", "--faceImg", required=True, 
    help="path to input image")
argP.add_argument("-d", "--detectModel", required=True, 
    help="path to Haar cascade .xml face detection model")    
args = vars(argP.parse_args())

# Tai anh len va chuyen sang gray scale
image = cv2.imread(args["faceImg"])
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tai face detector model len va tien hanh detect face
detectFace = cv2.CascadeClassifier(args["detectModel"])
rectsBox = detectFace.detectMultiScale(grayImg, 1.3, 5)

print("[INFO] Found {} faces".format(len(rectsBox)))

#Loop qua tat ca cac hinh chu nhat trong list rectsBox vua tim duoc(x,y,w,h)
#va ve hinh chu nhat 
for (x,y,w,h) in rectsBox:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 5)

cv2.imshow("Faces detector", image)
cv2.waitKey(0)