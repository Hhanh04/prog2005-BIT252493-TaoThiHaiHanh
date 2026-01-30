import math
num = float(input("Nhập một số: "))
if num < 0:
    print("Không thể tính căn bậc hai của số âm.")
else:
    sqrt = math.sqrt(num)
    print(f"Căn bậc hai của {num} là {sqrt:.2f}")
