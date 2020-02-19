#Run script: python3 CvBasic.py
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
"""
#Access pixel value (B,G,R) locate at [100,100]
(B,G,R) = image[100,100]
print("B={}, G={}, R={}".format(B,G,R))
cv2.waitKey(0)

#ROI, show image region of interest
#Must be have basic numpy and array
#https://datascienceplus.com/vectors-and-arrays-in-python/
roi = image[196:685,608:821] # [start_y: end_y, start_x: end_x]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

#Resize image for diferrent purpose such as:
#fixed screen size, faster processing with fewer pixel

rszImg = cv2.resize(image,(300,300))#ignore aspect ratio
cv2.imshow("Resized Imgae",rszImg)
cv2.waitKey(0)

#use imutils
rszKeepAptImg =imutils.resize(image,width=300)#keep aspect ratio
cv2.imshow("Resize Imgae Keep Aspect ration",rszKeepAptImg)
cv2.waitKey(0)

#Rotate image
rotateImg = imutils.rotate(image,45)#+/- <-/->
cv2.imshow("Rotate 45 image",rotateImg)
cv2.waitKey(0)

#Blurred image
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html?highlight=gaussianblur
blurredImg = cv2.GaussianBlur(image, (11,11), 0)
cv2.imshow("Blurred Image", blurredImg)
cv2.waitKey(0)
"""
#Drawing on a Image

#red rectangle around boy, thick=3
cv2.rectangle(image, (608,196), (821,685), (0,255,0), 3)
# green circle with center(700,500), r=40
cv2.circle(image, (700,500), 40, (0,0,255), -1)
# blue line cross the rect 
cv2.line(image, (608,196), (821,685), (255,0,0), 3)
#text start at axis(100,100), font=0.9 thick=3
cv2.putText(image,"Open CV Drawing", (100,100),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0),3)
cv2.imshow("Drawing on Img", image)
cv2.waitKey(0)
