"""
 Yeu cau:
- Dem cac vat the (khoi hinh hoc) xuat hien trong 1 buc anh
- User se intput duong dan toi buc anh
- Chuong trinh se ve duong bao xung quanh cac khoi hinh trong anh va xuat ra
gia tri so luong cac khoi hinh hoc trong anh
"""

import argparse
import cv2
import numpy
from matplotlib import pyplot as plt

# Tao object argparse de xay dung list argument
argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required=True, help="path to input image")
argDict = vars(argP.parse_args())
print(argDict["image"])

# Doc hinh len
image = cv2.imread(argDict["image"])
#De su dung giai thuat Canny, chuyen hinh sang gray scale
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Gray img", grayImg)
# cv2.waitKey(0)

#Lam mo anh de giam nhieu va xu ly nhanh hon
blurImage = cv2.GaussianBlur(grayImg,(3,3), 0)
# cv2.imshow("Blur img", blurImage)
# cv2.waitKey(0)

# Thuc hien Canny de tim cac goc cac canh cua anh de minh se xac dinh dc
# duong bien gioi xung cac khoi hinh hoc trong anh
edges = cv2.Canny(blurImage,50,130)


# plt.subplot(121),plt.imshow(blurImage,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()

# su dung contours de noi cac diem anh nay lai tao thanh duong bao vat the
# co duoc tap diem (x,y) tren duong bao cac khoi hinh
cntrsPoint =cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(type(cntrsPoint))

# for c in cntrsPoint:

#     # ve duong bao quanh cac tap diem (x,y)
#     cv2.drawContours(image,[c],-1, (205,0,255),3)
# cv2.drawContours(image, cntrsPoint, -1, (0,255,0), 3)

cv2.imshow("Contours Image",image)
cv2.waitKey(0)