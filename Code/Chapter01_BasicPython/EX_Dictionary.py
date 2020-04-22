if __name__=="__main__":
    N = int(input())
    bangDiem = {}
    for i in range(N):
        ten, toan, ly, hoa = input().split()
        diem = list([float(toan), float(ly), float(hoa)])
        print(diem)
        bangDiem[ten] = diem
