"""
Chay chuong trinh python3 ImgSub.py -b Images/BackGround.jpeg -f Images/ForeGround.jpeg
Chuong trinh nhan 2 tham so truyen vao la back ground va fore ground
image, xac dinh va ve hinh chu nhat bao quanh khu vuc khac biet giua 2 hinh
"""
import numpy as np
import argparse
import imutils 
import cv2
# from matplotlib import pyplot as plt

# Tao doi tuong argP dung de xay dung list argument can truyen vao cho chuong trinh
# Sau do parse argment ra 1 dictinary de su dung trong chuong trinh
argP = argparse.ArgumentParser()
argP.add_argument("-b", "--bgImg", required=True, 
    help="path to back ground input image")
argP.add_argument("-f", "--fgImg", required=True, 
    help="path to fore ground input image")    
args = vars(argP.parse_args())

# Tai anh len
bgImg = cv2.imread(args["bgImg"])
fgImg = cv2.imread(args["fgImg"])

# Chuyen sang gray scale, moi diem anh 0-255
bgGrayImg = cv2.cvtColor(bgImg, cv2.COLOR_BGR2GRAY)
fgGrayImg = cv2.cvtColor(fgImg, cv2.COLOR_BGR2GRAY)

#Tru nen
# 2 thang(0,255) tru nhau thi range la (-255,255) dua ve range (0,255) 
# bang cach lay tri tuyet doi
subImg = bgGrayImg.astype("int32") - fgGrayImg.astype("int32")
subImg = np.absolute(subImg).astype("uint8")

# theo nguyen tac nhung diem anh gia tri pixel cang khac nhau thi tru ra
# ket qua cang lon, ta dung threshold xac dinh nhung vung nay de tao ra
# binary image 
threshold = cv2.threshold(subImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Loai bo nhieu
threshold = cv2.erode(threshold, None, iterations=1)
threshold = cv2.dilate(threshold, None, iterations=1)

"""
plt.subplot(121),plt.imshow(subImg,cmap = 'gray')
plt.title('Sub Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(threshold,cmap = 'gray')
plt.title('Threshold Image'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
"""

# sau khi co duoc binary image voi cac diem anh danh dau, 
# thuc hien giai thuat contours de
# noi cac diem anh nay lai tao thanh duong bao qua cac vung danh dau.
# Contours se tra ve tap hop cac diem(x,y) tren duong bao
# duoc su dung cho qua trinh tinh toan tiep theo
contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# gia tri nguong duong vo cung, am vo cung
(minX, minY) = (np.inf, np.inf)
(maxX, maxY) = (-np.inf, -np.inf)

# loop tat ca item trong contours set de update min max xy
for c in contours:
    # xac dinh hinh chu nhat bao quanh moi item
    (x,y,w,h) = cv2.boundingRect(c)

    # w,h <= 20 =>noise=>boqua
    if w > 20 and h > 20:
        #update min,max XY value
        minX = min(minX,x)
        minY = min(minY,y)
        maxX = max(maxX, x+w-1)
        maxY = max(maxY, y+h-1)
    
#ve hinh chu nhat bao quanh khu vuc khac biet giua 2 anh
cv2.rectangle(fgImg, (minX, minY), (maxX, maxY), (255,0,0), 3)

#show img
cv2.imshow("Output Img",fgImg)
cv2.waitKey(0)
