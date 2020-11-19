"""
Cho 1 bang diem Toan Ly Hoa cua N sinh vien, tim diem trung binh.

Định dạng input:
N: số sinh viên, kiểu integer
Name1 DiemToan DiemLy DiemHoa
.
.
.
NameN DiemToan DiemLy DiemHoa
Name
Định dạng output:
Điểm trung bình

Ví dụ:
Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Output 0
56.00
Giải thích (52+56+60)/3
""" 

if __name__=="__main__":
    N = int(input())
    bangDiem = {}
    for i in range(N):
        ten, toan, ly, hoa = input().split()
        diem = list([float(toan), float(ly), float(hoa)])
        print(diem)
        bangDiem[ten] = diem
