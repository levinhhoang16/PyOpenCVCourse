# Run script: python3 FaceDetect.py --image Images/TwoFaces --detectModel HaarCascadeFrontalfaceDefault.xml
import argparse
import cv2


# create arg parser and parse the arg
argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required=True, 
    help="path to input image")
argP.add_argument("-d", "--detectModel", required=True, 
    help="path to Haar cascade .xml face detector model")    
args = vars(argP.parse_args())

# load img and convert to gray
image = cv2.imread(args["image"])
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load face detector and detect face
detector = cv2.CascadeClassifier(args["detectModel"])
rectsBox = detector.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors=9, minSize=(40,40), flags=cv2.CASCADE_SCALE_IMAGE)
print("[INFO] detected {} faces".format(len(rectsBox)))

#loop over rect bounding box(x,y,w,h) and draw blue rect with thick=3
for (x,y,w,h) in rectsBox:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 3)

cv2.imshow("Faces detector", image)
cv2.waitKey(0)