try:
    num1 = int(input("Nhập số nguyên thứ nhất: "))
    num2 = int(input("Nhập số nguyên thứ hai: "))
    if num2 == 0:
        print("Không thể chia cho 0.")
    else:
        result = num1 / num2
        print(f"Kết quả chia: {result}")
except ValueError:
    print("Dữ liệu nhập không hợp lệ. Vui lòng nhập số nguyên.")
