# python3 Cv**.py
# Load anh tu disk len ram, no la cai mang nhieu chieu chua cac diem anh
# Print thong so :(w,h,d)
# xuat anh ra man hinh

import cv2
import os
import imutils

imgPath = os.path.sep.join(["Images","TwoFaces.jpg"])
image = cv2.imread(imgPath)
(w,h,d) = image.shape
print("width={}, height={}, depth={}".format(w,h,d))
cv2.imshow("Two faces img", image)
cv2.waitKey(0)


#Truy xuat gia tri diem anh [B,G,R] o vi tri [100,100]
[B,G,R] = image[100,100]
print("B={}, G={} R={}".format(B,G,R))
cv2.waitKey(0)

#Cat cai mang anh ra va lay 1 phan trong do
# Phan do goi la ROI 
roi = image[100:675, 300:600]
cv2.imshow("ROI be trai", roi)
cv2.waitKey(0)

#Resize anh bo qua ti le 
rszImage = cv2.resize(image,(300,300)) 
cv2.imshow("Resized Image 300 300",rszImage)
cv2.waitKey(0)

#Resize giu ti le
rszImageKeepRatio = imutils.resize(image, width=300)
cv2.imshow("Resized Image 300 keep ratio",rszImageKeepRatio)
cv2.waitKey(0)

#Xoay anh
rotateImg = imutils.rotate(image,45)
cv2.imshow("Image rotate 45",rotateImg)
cv2.waitKey(0)

#Lam mo anh
bluredImage = cv2.GaussianBlur(image, (3,3), 0)
cv2.imshow("Blurred Image",bluredImage)
cv2.waitKey(0)

# Ve hinh chu nhat xung quanh be trai
cv2.rectangle(image, (608,196), (821,687), (0,255,0), 5)
cv2.imshow("Rect",image)
cv2.waitKey(0)

