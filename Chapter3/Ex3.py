mau_sac = ["Red", "Blue", "Green", "Yellow", "Purple"]

try:
    mau_sac.remove("Green")
    print("Danh sách sau khi xóa Green:", mau_sac)
except ValueError:
    print("Lỗi: Màu 'Green' không có trong danh sách.")
    print("Danh sách hiện tại:", mau_sac)
