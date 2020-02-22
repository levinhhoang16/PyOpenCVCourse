import numpy as np
import argparse
import imutils 
import cv2
from matplotlib import pyplot as plt

# create arg parser and parse the arg
argP = argparse.ArgumentParser()
argP.add_argument("-b", "--bgImg", required=True, 
    help="path to back ground input image")
argP.add_argument("-f", "--fgImg", required=True, 
    help="path to fore ground input image")    
args = vars(argP.parse_args())

# load image
bgImg = cv2.imread(args["bgImg"])
fgImg = cv2.imread(args["fgImg"])

# convert to gray
bgGrayImg = cv2.cvtColor(bgImg, cv2.COLOR_BGR2GRAY)
fgGrayImg = cv2.cvtColor(fgImg, cv2.COLOR_BGR2GRAY)

#subtraction
subImg = bgGrayImg.astype("int32") - fgGrayImg.astype("int32")
subImg = np.absolute(subImg).astype("uint8")

# using threshold img to find the region in subtract img with
# large pixel differences
threshold = cv2.threshold(subImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# remove noise 
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

# find contours in the threshold subtration img and draw the bounding box around the 
# fore ground area
contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
(minX, minY) = (np.inf, np.inf)
(maxX, maxY) = (-np.inf, -np.inf)

# loop over the contours and update min max X,Y value
for c in contours:
    # draw the bounding box around this item
    (x,y,w,h) = cv2.boundingRect(c)

    # w,h <= 20 =>noise=>ignore
    if w > 20 and h > 20:
        #update min,max XY value
        minX = min(minX,x)
        minY = min(minY,y)
        maxX = max(maxX, x+w-1)
        maxY = max(maxY, y+h-1)
    
#draw the bounding rectangle
cv2.rectangle(fgImg, (minX, minY), (maxX, maxY), (255,0,0), 3)

#show img
cv2.imshow("Output Img",fgImg)
cv2.waitKey(0)
