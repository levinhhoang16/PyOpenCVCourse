#Basic OpenCV
#Run script: python3 CvBasic.py

#Load imgae from disk to ram, image is multi dimession numPy arr
#print (width, height, depth) of images
#Show images on screen

import cv2
import imutils
import os

imgPath = os.path.sep.join(["Images","TwoFaces.jpg"])
image = cv2.imread(imgPath)
(width,height,depth) = image.shape
print("width={}, height={}, depth={}".format(width,height,depth))
cv2.imshow("BasicImage",image)
cv2.waitKey(0)

#Access pixel value (B,G,R) locate at [100,100]
(B,G,R) = image[100,100]
print("B={}, G={}, R={}".format(B,G,R))
cv2.waitKey(0)

#ROI, show imgae region of interest
roi = image[100:100,200:200]
cv2.imshow("ROI", roi)
cv2.waitKey(0)