import argparse
import imutils 
import cv2
import numpy as numpy
from matplotlib import pyplot as plt

# create arg parser and parse the arg
argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required=True, 
    help="path to input image")
args = vars(argP.parse_args())

#load input image and convert to grayscale
#using cvtColor function 
image = cv2.imread(args["image"])
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur image to reduce noise
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
# find countours in the edged and init total shapes count
cntrs = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntrs = imutils.grab_contours(cntrs)
total = 0

# loop all countrs item
for c in cntrs:
    #area too small=>noise=>ignore
    if cv2.contourArea(c) < 50:
        continue
    
    #else draw the contour on the image and increment count
    cv2.drawContours(image,[c], -1, (204, 0, 255), 2)
    total +=1

print("found {} shapes object".format(total))
cv2.imshow("Countour Image", image)
cv2.waitKey(0)