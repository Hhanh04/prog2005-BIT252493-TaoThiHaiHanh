def tong(n):
    if n == 0:
        return 0
    else:
        return n + tong(n - 1)
n = int(input("Nhập số n: "))
if n < 0:
    print("n phải là số không âm.")
else:
    print(f"Tổng từ 1 đến {n} là: {tong(n)}")
