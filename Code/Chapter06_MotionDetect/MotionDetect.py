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
"""

"""
Input: 
- Giải thuật trừ ảnh: GMG hoặc MOG
- Đường dẫn thư mục output
- Đường dãn video cần tác foregroud và capture hình ảnh chuyển động(nếu sử dụng video để test)

Output:
- File ảnh capture hình ảnh chuyển động lưu trong thư mục output kèm theo ngày giờ dưới format:
    yyyy-mm-dd_hh:mm:ss.jpg
"""
# OpenCV background subtractors
OPENCV_BG_SUBTRACTORS = {
	"GMG": cv2.bgsegm.createBackgroundSubtractorGMG,
	"MOG": cv2.bgsegm.createBackgroundSubtractorMOG
}