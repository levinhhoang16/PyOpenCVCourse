"""
- Có 2 chế độ:
    - Sử dụng Pi camera để record video theo dõi dụng cụ cho chim ăn
    - Sử dụng file video có sẵn
- Capture mỗi frame, sử dụng giải thuật trừ ảnh nền cung cấp bởi opencv để phát hiện sự kiện chim đến ăn.
- Các giải thuật trừ ảnh nền có thể sử dụng:
    - GMG
    - MOG

    [BackgroundSubtractor trong opencv](https://www.notion.so/BackgroundSubtractor-trong-opencv-060e34989cc84828abd8c552b3bcb651)

- Lưu lại 1 frame trước trong và sau khi phát hiện sự kiện
- Đặt tên file theo format **yyyy-mm-dd_hh:mm:ss.jpg**
- Thư mục lưu file video được user truyền vào argument khi chạy chương trình
Input: 
- Giải thuật trừ ảnh: GMG hoặc MOG
- Đường dẫn thư mục output
- Đường dãn video cần tác foregroud và capture hình ảnh chuyển động(nếu sử dụng video để test)

Output:
- File ảnh capture hình ảnh chuyển động lưu trong thư mục output kèm theo ngày giờ dưới format:
    yyyy-mm-dd_hh:mm:ss.jpg

##########################################################################################
Các bước thực hiên:
- Viết chương trình để làm quen với thuật toán trừ ảnh nền
- Khử nhiễu cho foreground mask xuất ra từ thuật toán trừ ảnh nền
- Vẽ contour bao quanh foreground
- Buffer và lưu frame trước và sau khi phát hiện event
- Lưu ảnh capture khi xảy ra event
"""
# Chương trình làm quen với thuật toán trừ ảnh nền cung cấp bởi opencv
# Chạy chương trình với tham số mặc định Python3 MotionDetect1.py
# https://docs.opencv.org/4.1.0/d1/dc5/tutorial_background_subtraction.html

from __future__ import print_function
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str,
                    help='Path to a video or a sequence of image.', default='/home/pi/birds_10min.mp4')
parser.add_argument('--algo', type=str,
                    help='Background subtraction method (MOG, GMG).', default='MOG')
args = parser.parse_args()

# [create]
# create Background Subtractor objects
if args.algo == 'MOG':
    backSub = cv.bgsegm.createBackgroundSubtractorMOG()
else:
    backSub = cv.bgsegm.createBackgroundSubtractorGMG()
# [create]

# [capture]
capture = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))
if not capture.isOpened:
    print('Unable to open: ' + args.input)
    exit(0)
# [capture]

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    # [apply]
    # update the background model
    fgMask = backSub.apply(frame)
    # [apply]

    # [display_frame_number]
    # get the frame number and write it on the current frame
    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    # [display_frame_number]

    # [show]
    # show the current frame and the fg masks
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    # [show]

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
