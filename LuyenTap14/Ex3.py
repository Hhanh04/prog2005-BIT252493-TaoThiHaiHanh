arr = list(map(int, input("Nhập các số (cách nhau bởi dấu cách): ").split()))
so_le = [x for x in arr if x % 2 != 0]
print("Các số lẻ:", so_le, "- Số lượng:", len(so_le))
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

so_nt = [x for x in arr if la_so_nguyen_to(x)]
print("Các số nguyên tố:", so_nt)