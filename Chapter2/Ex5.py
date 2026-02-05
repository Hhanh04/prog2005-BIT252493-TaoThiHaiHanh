chuoi = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")
count = 0
for char in chuoi:
    if char == ky_tu:
        count += 1
print(f"Ký tự '{ky_tu}' xuất hiện {count} lần trong chuỗi.")
