# Run script: python3 PiCamAdjust.py

from imutils.video import VideoStream
from itertools import cycle
from pprint import pprint
import time
import cv2

global g_viStream

def getPicamSettings(output=False):
    global g_picamSettings
    global g_viStream

    #local var to hold current setting
    curPicamSettings = {}

    #print status message if output enable
    if output:
        print("[INFO] Read Pi cam settings...")
    
    #Get picam attributes from g_viStream object

    for attr in g_picamSettings.keys():
        curPicamSettings[attr] = getattr(g_viStream.camera, attr)
    
    # print setting if output enable
    if output:
        pprint(curPicamSettings)

    g_picamSettings = curPicamSettings

    return curPicamSettings

def getSinglePicamSettings(setting):
    curPicamSettings = getPicamSettings()
    return curPicamSettings[setting]

#function to activate new Picam settings
def activatePicamSettings(**args):
    global g_viStream
    g_viStream.stop()
    time.sleep(0.25)
    g_viStream = VideoStream(usePiCamera=True, **args).start()
    time.sleep(2)
    print("[INFO] suceed! ")

def setPicamSettings(**args):
    global g_picamSettings
    global g_viStream

    # store current setting
    print("[INFO] read settings...")
    curPicamSettings = getPicamSettings()

    # print and update new setting value
    for (attr,value) in args.items():
        print("[INFO] Old setting {}->New setting {}".format(curPicamSettings[attr],value))
        curPicamSettings[attr] = value

    # init variable to hold the duplicated attr in curPicamSettings and delete it
    attrsToDel = []
    for attr in curPicamSettings.keys():
        if curPicamSettings[attr] == None:
            attrsToDel.append(attr)
    pprint(attrsToDel)
    for attr in attrsToDel:
        curPicamSettings.pop(attr)

    args = curPicamSettings
    activatePicamSettings(**args)

# Init VideoStream
g_viStream = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# Default setting value for auto white balance and ISO mode 
awbModes = ["off", "auto", "sunlight", "cloudy", "shade",
	"tungsten", "fluorescent", "flash", "horizon"]
isoModes = [0, 100, 200, 320, 400, 500, 640, 800, 1600]

# init 2 cycles pools
isoModesPool = cycle(isoModes)
awbModesPool = cycle(awbModes)

# the following dictionary consists of PiCamera attributes that can be
# *changed*; the list is not exhaustive because some settings can only
# be changed based on the values of others, so be sure to refer to
# the docs
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


# Loop over frames
while True:
    # get a frame
    frame = g_viStream.read()

    #show
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)

    # Handle keypress
    if key == ord("q"):
        break
    elif key == ord("w"): # auto white balance
        awbMode = getSinglePicamSettings("awb_mode")
        setPicamSettings(awb_mode=next(awbModesPool))
    elif key == ord("i"): # ISO
        isoMode = getSinglePicamSettings("iso")
        setPicamSettings(iso=next(isoModesPool))
    elif key == ord("b"): # brightness
        brightness = getSinglePicamSettings("brightness")
        setPicamSettings(brightness=brightness+1)
    elif key == ord("d"): # darken brightness
        brightness = getSinglePicamSettings("brightness")
        setPicamSettings(brightness=brightness-1)
    elif key == ord("r"): # read setting
        settings = getPicamSettings(output=True)

g_viStream.stop()
cv2.destroyAllWindows()                