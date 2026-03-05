input_str = input("Nhập danh sách số (cách nhau bởi dấu cách): ")
danh_sach = [int(x) for x in input_str.split()]

print("Các số lẻ trong danh sách:")
for so in danh_sach:
    if so % 2 != 0:
        print(so, end=" ")
print()
