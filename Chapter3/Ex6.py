def bubble_sort_with_count(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return arr, swap_count
input_str = input("Nhập các số nguyên (cách nhau bởi dấu cách): ")
so_nguyen = [int(x) for x in input_str.split()]

print("Danh sách ban đầu:", so_nguyen)
ket_qua, so_lan_hoan_doi = bubble_sort_with_count(so_nguyen)
print("Danh sách sau khi sắp xếp:", ket_qua)
print(f"Số lần hoán đổi: {so_lan_hoan_doi}")
