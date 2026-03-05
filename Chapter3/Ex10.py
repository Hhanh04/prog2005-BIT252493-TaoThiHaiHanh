input_str = input("Nhập danh sách số (cách nhau bởi dấu cách): ")
danh_sach = [int(x) for x in input_str.split()]

tong_chan = 0
print("Các số chẵn:")
for so in danh_sach:
    if so % 2 == 0:
        print(so, end=" ")
        tong_chan += so

print(f"\nTổng các số chẵn: {tong_chan}")
