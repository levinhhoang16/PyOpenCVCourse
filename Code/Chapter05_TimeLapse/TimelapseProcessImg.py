# Chương trình tạo video từ các frame trong thư mục output directory
# được tạo ra sau khi chạy script TimelapseCaptureFrame.py
# Chạy chương trình bằng lệnh sau
# python3 TimelapseProcessImg.py \
# 	--input output/images/2020-04-26-2225 --output output/videos \
# 	--fps 30

# import các package cần thiết
from imutils import paths
import progressbar
import argparse
import cv2
import os

# function để lấy frame number từ tên image file
# Image file path: output/images/2020-04-26-2225/0000000000000027.jpg ==>27
def get_img_file_num(imagePath):
	return int(imagePath.split(os.path.sep)[-1][:-4])

# Khởi tạo ArgumentParser và thêm các argument cần thiết
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, 
	help="Path to the input directory of image files")
ap.add_argument("-o", "--output", required=True, 
	help="Path to the output video directory")
ap.add_argument("-f", "--fps", type=int, default=30, 
	help="Frames per second of the output video")
args = vars(ap.parse_args())

# Khởi tạo videowriter sử dụng fourcc codec, định dạng video là MJPG 
# Các video được nén lại để giảm dung lượng, mã hóa sử dụng codec
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = None

# Lấy các đường dẫn images và thư mục output từ các tham số truyền vào để
# tạo output file name và output path
imagePaths = list(paths.list_images(args["input"]))
outputFile = "{}.avi".format(args["input"].split(os.path.sep)[2])
outputPath = os.path.join(args["output"], outputFile)
print("[INFO] building {}...".format(outputPath))

# Khởi tạo thanh progess bar hiện thị % quá trình build video
# https://rdrr.io/cran/pbmcapply/man/progressBar.html
# ETA: dự đoán thời gian hoàn thành
# max value là số lượng image input
widgets = ["Building Video: ", progressbar.Percentage(), " ", 
	progressbar.Bar(), " ", progressbar.ETA()]
pbar = progressbar.ProgressBar(maxval=len(imagePaths), 
	widgets=widgets).start()

# Duyệt qua tất cả các imgae input đã được sắp theo thứ tự ghi vào dựa trên
# number trong filename
for (i, imagePath) in enumerate(sorted(imagePaths, key=get_img_file_num)):
	# tải image lên
	image = cv2.imread(imagePath)

	# khởi tạo video writer nếu cần thiết
	if writer is None:
		(H, W) = image.shape[:2]
		writer = cv2.VideoWriter(outputPath, fourcc, args["fps"],
			(W, H), True)

	# ghi image vào output video
	writer.write(image)
	# update progress bar
	pbar.update(i)

# release memory cho writer object
print("[INFO] cleaning up...")
pbar.finish()
writer.release()
