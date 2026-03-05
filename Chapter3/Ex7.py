def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
input_str = input("Nhập danh sách số (cách nhau bởi dấu cách): ")
danh_sach = [int(x) for x in input_str.split()]
tim_kiem = int(input("Nhập số cần tìm: "))

index = linear_search(danh_sach, tim_kiem)

if index != -1:
    print(f"Số {tim_kiem} tìm thấy tại chỉ số: {index}")
else:
    print(f"Số {tim_kiem} không có trong danh sách.")
