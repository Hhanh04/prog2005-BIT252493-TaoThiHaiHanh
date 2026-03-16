class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    def __eq__(self, other):
        """Nạp chồng toán tử == để so sánh theo điểm"""
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

    def __str__(self):
        return f"SinhVien(diem={self.diem})"


print("=== BÀI 10 ===")
sv1 = SinhVien(8.5)
sv2 = SinhVien(8.5)
sv3 = SinhVien(9.0)

print(f"sv1 == sv2: {sv1 == sv2}")  # True
print(f"sv1 == sv3: {sv1 == sv3}")  # False
print(f"sv1: {sv1}")
print(f"sv2: {sv2}")
