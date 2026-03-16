# Bài 2:
def bai2():
    print("Bài 2: Tính tổng các chữ số")
    num = input("Nhập một số: ")
    total = sum(int(digit) for digit in num if digit.isdigit())
    print(f"Tổng các chữ số: {total}")
    print("-" * 50)