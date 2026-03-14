class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau

    def __str__(self):
        return f"Hoa: {self.ten}, Màu: {self.mau}"


# Tạo đối tượng và in thông tin
hoa_hong = Hoa("Hoa hồng", "Đỏ")
print(hoa_hong)
