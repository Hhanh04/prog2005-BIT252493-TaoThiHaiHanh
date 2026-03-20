s = input("Nhập chuỗi: ")
c = input("Nhập ký tự: ")

dem = 0
for i in s:
    if i == c:
        dem += 1

print("Số lần xuất hiện:", dem)