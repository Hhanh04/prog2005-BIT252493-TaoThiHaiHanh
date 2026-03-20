while True:
    print("1.Bài1  2.Bài2  0.Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        path = input("Nhập path: ")
        print(path.split("\\")[-1])

    elif chon == "2":
        s = input("Chuỗi: ")
        c = input("Ký tự: ")
        print(s.count(c))

    elif chon == "0":
        break