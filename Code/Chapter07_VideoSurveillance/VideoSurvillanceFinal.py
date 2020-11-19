# Chương trình minh họa giải thuât BgSubtractorAbsDiff với accumulateWeighted
# sử dụng thread
# # Thread để feed frame từ camera vao buffer sử dụng imutils VideoStream
# # Thread để lấy frame từ buffer và detect fore ground
# Chay chuong trinh
# win 10: Mở Anaconda shell, gõ cmd: py BgSubtractorThread.py
# organize imports
import threading
import time
import logging
import cv2
import numpy as np
import imutils
from imutils.video import VideoStream
from flask import Response
from flask import render_template
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)
lock = threading.Lock()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/video_stream')
def video_stream():
    global g_outputFrame
    def generate():
        while True:
            with lock:
                frame = g_outputFrame
                if frame is None:
                    continue
            if frame is not None:
                ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    return Response(generate(),  mimetype='multipart/x-mixed-replace; boundary=frame')


# Khởi tạo các biến global
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

#
g_outputFrame = None
# Start video stream thread để feed frame từ camera vào buffer
g_vs = VideoStream(src=0).start()
time.sleep(2.0)


def detect(bg, image, tVal=25):
    # compute the absolute difference between the background model
    # and the image passed in, then threshold the delta image
    delta = cv2.absdiff(bg.astype("uint8"), image)
    thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1]

    # perform a series of erosions and dilations to remove small
    # blobs
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # find contours in the thresholded image and initialize the
    # minimum and maximum bounding box regions for motion
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    (minX, minY) = (np.inf, np.inf)
    (maxX, maxY) = (-np.inf, -np.inf)

    # if no contours were found, return None
    if len(cnts) == 0:
        return None

    # otherwise, loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and use it to
        # update the minimum and maximum bounding box regions
        (x, y, w, h) = cv2.boundingRect(c)
        (minX, minY) = (min(minX, x), min(minY, y))
        (maxX, maxY) = (max(maxX, x + w), max(maxY, y + h))

    # otherwise, return a tuple of the thresholded image along
    # with bounding box
    return (thresh, (minX, minY, maxX, maxY))


def captureFrameAndDetect():
    global g_vs
    global g_outputFrame
    # read the frames from the camera
    img = g_vs.read()

    # modify the data type
    # setting to 32-bit floating point
    # averageValue1 = np.float32(img)
    averageValue1 = None
    # loop runs if capturing has been initialized.
    while True:
        # reads frames from a camera
        img = g_vs.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if averageValue1 is None:
            averageValue1 = img.copy().astype("float")
            continue
        # using the cv2.accumulateWeighted() function
        # that updates the running average
        cv2.accumulateWeighted(img, averageValue1, 0.02)

        # converting the matrix elements to absolute values
        # and converting the result to 8-bit.
        resultingFrames1 = cv2.convertScaleAbs(averageValue1)
        # Show two output windows
        # the window showing output of alpha value 0.02
        # cv2.imshow('averageValue1', resultingFrames1)

        x = detect(averageValue1, img)
        if x:
            (thresh, (minX, minY, maxX, maxY)) = x
            # cv2.imshow('thresh', thresh)
            cv2.rectangle(img, (minX, minY, maxX, maxY), (255, 0, 0), 3)
        # the input / original frames window
        # cv2.imshow('InputWindow', img)
        with lock:
            g_outputFrame = img.copy()
        time.sleep(1)
        # # Wait for Esc key to stop the program
        # k = cv2.waitKey(30) & 0xff
        # if k == ord('q'):
        #     break


if __name__ == "__main__":
    fetchForeGroundThread = threading.Thread(
        name='Detect and fetch foreground', target=captureFrameAndDetect)
    fetchForeGroundThread.setDaemon(True)
    fetchForeGroundThread.start()

    app.run(host="0.0.0.0", port=5000, debug=True,
            threaded=True, use_reloader=False)
    fetchForeGroundThread.join()

# Close the window
g_vs.stop()
