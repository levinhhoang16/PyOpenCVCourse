# Chương trình minh họa giải thuât BgSubtractorAbsDiff với accumulateWeighted
# Chay chuong trinh
# win 10: Mở Anaconda shell, gõ cmd: py BgSubtractorAbsDiff.py
# organize imports
import cv2
import numpy as np
import imutils


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


if __name__ == "__main__":
    # capture frames from a camera
    cap = cv2.VideoCapture(0)

    # read the frames from the camera
    _, img = cap.read()

    # modify the data type
    # setting to 32-bit floating point
    # averageValue1 = np.float32(img)
    averageValue2 = np.float32(img)
    averageValue1 = None
    # loop runs if capturing has been initialized.
    while(1):
        # reads frames from a camera
        _, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if averageValue1 is None:
            averageValue1 = img.copy().astype("float")
            continue
        # using the cv2.accumulateWeighted() function
        # that updates the running average
        cv2.accumulateWeighted(img, averageValue1, 0.02)
        # cv2.accumulateWeighted(img, averageValue2, 0.2)

        # converting the matrix elements to absolute values
        # and converting the result to 8-bit.
        resultingFrames1 = cv2.convertScaleAbs(averageValue1)
        # resultingFrames2 = cv2.convertScaleAbs(averageValue2)
        # Show two output windows
        # the window showing output of alpha value 0.02
        cv2.imshow('averageValue1', resultingFrames1)
        # cv2.imshow('averageValue2', resultingFrames2)

        x = detect(averageValue1, img)
        if x:
            (thresh, (minX, minY, maxX, maxY)) = x
            cv2.imshow('thresh', thresh)
            cv2.rectangle(img, (minX, minY, maxX, maxY), (255,0,0), 3)
        # the input / original frames window
        cv2.imshow('InputWindow', img)
        # Wait for Esc key to stop the program
        k = cv2.waitKey(30) & 0xff
        if k == ord('q'):
            break

    # Close the window
    cap.release()

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()
