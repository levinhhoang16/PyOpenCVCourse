# Chay chuong trinh: python3 FaceDetect.py --image Images/TwoFaces --detectModel HaarCascadeFrontalfaceDefault.xml
import argparse
import cv2


# Tao doi tuong argP dung de xay dung list argument can truyen vao cho chuong trinh
# Sau do parse argment ra 1 dictinary de su dung trong chuong trinh
argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required=True, 
    help="path to input image")
argP.add_argument("-d", "--detectModel", required=True, 
    help="path to Haar cascade .xml face detector model")    
args = vars(argP.parse_args())

# Tai anh len va chuyen sang gray scale
image = cv2.imread(args["image"])
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tai face detector model len va tien hanh detect face
detector = cv2.CascadeClassifier(args["detectModel"])
rectsBox = detector.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors=9, 
            minSize=(40,40), flags=cv2.CASCADE_SCALE_IMAGE)
print("[INFO] detected {} faces".format(len(rectsBox)))

#loop qua tat ca cac hinh chu nhat bao(x,y,w,h) vua tim duoc
#  va ve blue rect voi do day net ve la 3
for (x,y,w,h) in rectsBox:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 3)

cv2.imshow("Faces detector", image)
cv2.waitKey(0)