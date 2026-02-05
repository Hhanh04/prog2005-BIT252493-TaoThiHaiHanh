num = input("Nhập một số nguyên dương 5 chữ số: ")
if len(num) != 5 or not num.isdigit():
    print("Số nhập phải là số nguyên dương có đúng 5 chữ số.")
else:
    max_digit = 0
    for digit in num:
        if int(digit) > max_digit:
            max_digit = int(digit)
    print(f"Chữ số lớn nhất là: {max_digit}")
