def bai3():
    """Bài 3: Bảng cửu chương 1-9"""
    print("BÀI 3: BẢNG CỬU CHƯƠNG")
    n = int(input("Nhập số (1-9): "))

    if 1 <= n <= 9:
        print(f"Bảng cửu chương {n}:")
        for i in range(1, 10):
            print(f"{n} x {i} = {n * i}")
    else:
        print("Số phải từ 1-9!")
    print("-" * 50)
