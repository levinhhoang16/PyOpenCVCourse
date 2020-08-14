# Chương trình capture frame từ camera, chèn timestamp và lưu frame vào 
# thư mục output do người dùng tùy chọn
# Chạy chương trình bằng lệnh sau 
# python3 TimelapseCaptureFrame.py --output output/images \
#	--delay 2 --display 1

# import các package cần thiết
# Sử dụng VideoStream class để đọc frame từ camera cùng với cv2 để
# ghi chú và save frames lên disk. 
# datetime và time được dùng cho timestamps và delay giữa các lần capture
# os module được dùng để tạo output dir
from imutils.video import VideoStream
from datetime import datetime
import argparse
import signal
import time
import cv2
import sys
import os

# function dùng để xỷ lý ngắt khi nhấn keyboard
def keyboard_handler(sig, frame):
	print("[INFO] You pressed `ctrl + c`! Your pictures are saved" \
		" in the output directory you specified...")
	sys.exit(0)

# Khởi tạo ArumnetParser và thiết lập các argument cần thiết để chay script
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, 
	help="path to the output directory")
ap.add_argument("-d", "--delay", type=float, default=5.0, 
	help="delay in seconds between frames captured")
ap.add_argument("-p", "--display", type=int, default=0,
	help="boolean used to indicate if frames should be displayed")
args = vars(ap.parse_args())

# Khởi tạo đường dẫn cho output directory và tạo output directory
outputDir = os.path.join(args["output"],
	datetime.now().strftime("%Y-%m-%d-%H%M"))
os.makedirs(outputDir)

# Khởi tạo video stream sử dụng Picam và chờ 2 s để khỏi động camera
print("[INFO] warming up camera...")
#vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True, resolution=(1920, 1280),
	framerate=30).start()
time.sleep(2.0)

# Đặt count về 0
count = 0

# Đăng kí signal để handle keyboard event
signal.signal(signal.SIGINT, keyboard_handler)
print("[INFO] Press `ctrl + c` to exit, or 'q' to quit if you have" \
	" the display option on...")

# vòng lặp duyệt qua tất cả các frame đọc được từ camera thông qua 
# VideoStream class
while True:
	# lấy frame tiếp theo
	frame = vs.read()

	# ghi timestamp cho frame vừa đọc được ở góc trái của frame, màu chứ đỏ,
	# font chữ HERSHEY_SIMPLEX, cỡ 0.4, độ dạy nét chữ là 1
	ts = datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
	cv2.putText(frame, ts, (10, frame.shape[0] - 10), 
		cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

	# ghi frame hiện tại vào thư mục ouput, đinh dạng tên file {count}.jpg,
	filename = "{}.jpg".format(str(count).zfill(16)) #độ rộng string là 16
	cv2.imwrite(os.path.join(outputDir, filename), frame)

	# Kiểm tra tham số display truyền vào để quyết định có xuất ra màn hình k 
	if args["display"]:
		# xuất frame ra màn hình
		cv2.imshow("Frame", frame)
		# chờ keyboard event trong 1 ms
		key = cv2.waitKey(1) & 0xFF

		# nếu bắt được event phím nhấn "q" thì thoát vòng lặp
		if key == ord("q"):
			break

	# tăng biến đếm và sleep tùy vào thời gian được truyền vào trong 
	# argument delay
	count += 1
	time.sleep(args["delay"])

# Đóng tất cả cửa sổ và release memory cho VideoStream object
print("[INFO] cleaning up...")
if args["display"]:
	cv2.destroyAllWindows()
vs.stop()
