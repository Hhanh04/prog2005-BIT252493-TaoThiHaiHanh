input_str = input("Nhập danh sách số (cách nhau bởi dấu cách): ")
danh_sach = [int(x) for x in input_str.split()]

if danh_sach:
    max_val = max(danh_sach)
    min_val = min(danh_sach)
    print(f"Giá trị lớn nhất: {max_val}")
    print(f"Giá trị nhỏ nhất: {min_val}")
else:
    print("Danh sách rỗng.")
