class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
sv1 = Student("Lee Thị Như Ý", 8.5)
sv2 = Student("Nguyễn Thị Minh Hy", 9.0)

print("BÀI 7 - KHỞI TẠO 2 SINH VIÊN:")
print(f"SV1: {sv1.name} - {sv1.score}")
print(f"SV2: {sv2.name} - {sv2.score}")
print("-" * 50)
