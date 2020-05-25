import cv2
from imutils.video import VideoStream
from pprint import pprint
import time

global g_videoStream

# Function de lay cac thong so setting cua Pi cam tu videostream object
def getPiCamSetting():

    #dictionary de giu cac setting hien tai
    curPicamSetings = {}

    print("Read Pi cam setting")
    # Lop qua tat cac cac key trong g_picamSettings de lay thuoc tinh cua key do
    # trong g_videoStream object
    for attr in g_picamSettings.keys():
        curPicamSetings[attr] = getattr(g_videoStream.camera, attr)
    
    # pprint(curPicamSetings)

    return curPicamSetings

# Function de kich hoat gia tri setting moi
def activateNewPiCamsetting(**kargs):
    global g_videoStream
    g_videoStream.stop()
    time.sleep(0.5)
    print("activateNewPiCamsetting")
    g_videoStream = VideoStream(usePiCamera=True, **kargs).start()
    time.sleep(2.0)

# Function de set new Picam Setting value va kich hoat no
def setPicamSetting(**kargs):
    #Truoc khi set setting moi, luu gia tri cua current Picam setting
    curPicamSetings = getPiCamSetting()
    # pprint(curPicamSetings)

    #Vong lap for loop qua cac gia tri setting(key,value) can thay doi trong tham so truyen vao
    for key, value in kargs.items(): 
        print("Old setting {} ===> New setting {}".format(curPicamSetings[key],value))
        curPicamSetings[key] = value
    
    # pprint(curPicamSetings)

    #Tien hanh xoa key co gia tri None trong curPicamSetings

    attrsToDel = []
    for attr in curPicamSetings.keys():
        if curPicamSetings[attr] == None:
            attrsToDel.append(attr)
    pprint(attrsToDel)
    for attr in attrsToDel:
        curPicamSetings.pop(attr)        

    activateNewPiCamsetting(**curPicamSetings)




#dictionary chua cac thong so Picam ma minh muon lay ve de thay doi no
#Lay tu Picam document:
#https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.iso
g_picamSettings = {
	"awb_mode": None,
	"awb_gains": None,
	"brightness": None,
	"color_effects": None,
	"contrast": None,
	"drc_strength": None,
	"exposure_compensation": None,
	"exposure_mode": None,
	"flash_mode": None,
	"hflip": None,
	"image_denoise": None,
	"image_effect": None,
	"image_effect_params": None,
	"iso": None,
	"meter_mode": None,
	"rotation": None,
	"saturation": None,
	"sensor_mode": None,
	"sharpness": None,
	"shutter_speed": None,
	"vflip": None,
	"video_denoise": None,
	"video_stabilization": None,
	"zoom": None
}

#Khoi tao doi tuong video stream object
g_videoStream = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)

while True:
    #doc frame
    frame = g_videoStream.read()

    #show frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    elif key == ord("a"):
        setPicamSetting(awb_mode="sunlight")
    elif key == ord("w"):
        setPicamSetting(awb_mode="cloudy")
    elif key == ord("b"):
        setPicamSetting(awb_mode="tungsten")