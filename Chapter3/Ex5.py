def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
input_str = input("Nhập các số thực (cách nhau bởi dấu cách): ")
so_thuc = [float(x) for x in input_str.split()]

print("Danh sách ban đầu:", so_thuc)
insertion_sort_desc(so_thuc)
print("Danh sách sau khi sắp xếp giảm dần:", so_thuc)
