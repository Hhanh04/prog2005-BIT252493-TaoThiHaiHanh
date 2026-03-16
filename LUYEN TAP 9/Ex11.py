class SinhVien:
    _dem_so_luong = 0  # Biến class để đếm

    @classmethod
    def dem_so_doi_tuong(cls):
        """Class method trả về số đối tượng đã tạo"""
        return cls._dem_so_luong

    def __init__(self, diem):
        self.diem = diem
        SinhVien._dem_so_luong += 1  # Tăng đếm khi tạo object mới

    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

    def __str__(self):
        return f"SinhVien(diem={self.diem})"


print("=== BÀI 11 ===")
print(f"Số SV ban đầu: {SinhVien.dem_so_doi_tuong()}")

sv1 = SinhVien(8.5)
sv2 = SinhVien(9.0)
sv3 = SinhVien(8.5)

print(f"Số SV sau khi tạo 3 đối tượng: {SinhVien.dem_so_doi_tuong()}")
print(f"sv1 == sv3: {sv1 == sv3}")

sv4 = SinhVien(7.5)
print(f"Số SV hiện tại: {SinhVien.dem_so_doi_tuong()}")
