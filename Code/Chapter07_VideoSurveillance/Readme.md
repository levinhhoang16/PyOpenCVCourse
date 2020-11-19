# Chương trình Giám sát video camera
## Yêu cầu:
    - Capture image từ camera
    - Detect vật thể chuyển động sử dụng back ground subtractor abs_diff và accumulateWeighted
    - Stream vide lên web browser sử dụng Flask
    
    **Input format:
        - Chương trình nhận vào các tham số:
            - Địa chỉ ipaddress của webserver
            - Port number của webserver
            - Số lượng frame_cnt để xây dựng back ground model
    **Output format:
        - Video được stream lên web page ở địa chỉ ip và port được user cung cấp
        - Mỗi khung hình detect được chuyển động sẽ dc mask bằng hình chữ nhật bao quanh foreground

## Các bước thực hiện:
    Tách chương trình thành 3 phần nhỏ:
    - Chương trình 1-Detect vật thể chuyển động sử dưng back ground subtractor abs_diff và accumulateWeighted
    - Chương trình 2-Stream video lên web sử dụng Flask
    - Chương trình hoàn thiện: Kết hợp chương trình 1 và 2