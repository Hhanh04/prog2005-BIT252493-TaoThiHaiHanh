chuoi = input("Nhập chuỗi: ")
dao_nguoc_1 = chuoi[::-1]
print(f"Cách 1 (Slicing): {dao_nguoc_1}")
dao_nguoc_2 = ""
for i in range(len(chuoi) - 1, -1, -1):
    dao_nguoc_2 += chuoi[i]
print(f"Cách 2 (Vòng lặp): {dao_nguoc_2}")
