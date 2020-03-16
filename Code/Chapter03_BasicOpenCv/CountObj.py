"""
Chay chuong trinh python3 CountObj.py --image Images/Shapes.jpg
Chuong trinh nhan tham so truyen vao la duong dan toi image can dem vat the
"""
import argparse
import imutils 
import cv2
import numpy as numpy
from matplotlib import pyplot as plt

# Tao doi tuong argP dung de xay dung list argument can truyen vao cho chuong trinh
# Sau do parse argment ra 1 dictinary de su dung trong chuong trinh 
argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required=True, 
    help="path to input image")
args = vars(argP.parse_args())

# Tai input image len va chuyen sang grayscale 
# su dung cvtColor function 
image = cv2.imread(args["image"])
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Lam mo anh de giam nhieu va xu ly nhanh hon
# Sau do thuc hien giai thuat canny de tim cac goc canh cua anh giup xac dinh 
# duoc duong bien gioi bao xung quanh cac khoi hinh hoc trong anh o buoc tiep theo
# Canny se tra ve 1 binary image voi tap hop cac diem anh duoc danh dau
blurImg = cv2.GaussianBlur(grayImg,(3,3), 0)
edges = cv2.Canny(blurImg,50,130)

"""
plt.subplot(121),plt.imshow(blurImg,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
"""

# sau khi co duoc binary image voi cac diem anh danh dau, 
# thuc hien giai thuat contours de
# noi cac diem anh nay lai tao thanh duong bao vat the.
# Contours se tra ve tap hop cac diem(x,y) tren duong bao
# duoc su dung cho qua trinh tinh toan tiep theo de dem vat the
cntrs = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntrs = imutils.grab_contours(cntrs)
total = 0

# loop tat ca cac item trong contours
for c in cntrs:
    #vung bao co dien tich qua nho, xem xet nhu nhieu va bo qua
    if cv2.contourArea(c) < 50:
        continue
    
    #ve duong bao quanh tap diem(x,y) va tang count len
    cv2.drawContours(image,[c], -1, (204, 0, 255), 2)
    total +=1

print("found {} shapes object".format(total))
cv2.imshow("Countour Image", image)
cv2.waitKey(0)