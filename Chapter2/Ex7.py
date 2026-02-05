a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if a <= 0 or b <= 0:
    print("Cả hai số phải là số nguyên dương.")
else:
    while b != 0:
        a, b = b, a % b
    print(f"UCLN là: {a}")
