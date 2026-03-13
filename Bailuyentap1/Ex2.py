def bai2():
    """Bài 2: Nhập 2 số, tính các phép toán"""
    print("BÀI 2: NHẬP 2 SỐ")
    x = float(input("Nhập số x: "))
    y = float(input("Nhập số y: "))

    print(f"\nKết quả với x={x}, y={y}:")
    print(f"Lũy thừa x^y = {x ** y}")
    print(f"Căn bậc 2 của x = {math.sqrt(x)}")
    print(f"Chia lấy phần nguyên x/y = {x // y}")
    print(f"Chia lấy phần dư x%y = {x % y}")
    print(f"Làm tròn x = {round(x)}")
    print("-" * 50)
