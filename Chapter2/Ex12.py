n = int(input("Nhập số n: "))
total = 0
for i in range(1, n + 1, 2):
    total += i
print(f"Tổng các số lẻ từ 1 đến {n} là: {total}")
