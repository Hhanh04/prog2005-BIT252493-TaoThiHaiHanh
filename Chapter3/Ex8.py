input_str = input("Nhập danh sách số (cách nhau bởi dấu cách): ")
danh_sach = [int(x) for x in input_str.split()]

found = False
for so in danh_sach:
    if so > 10:
        print(f"Số đầu tiên lớn hơn 10 là: {so}")
        found = True
        break

if not found:
    print("Không có số nào lớn hơn 10 trong danh sách.")
