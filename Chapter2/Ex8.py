num = int(input("Nhập một số dương: "))
if num <= 0:
    print("Số phải là số dương.")
else:
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(f"Số đảo ngược là: {reversed_num}")
