class Student:
    def __init__(self, name, score):
        self.name = name
        if 0 <= score <= 10:
            self.score = score
        else:
            print(f"LỖI: Điểm {score} không hợp lệ! Phải từ 0-10")
            self.score = 0

print("BÀI 8 - XÁC THỰC ĐIỂM:")
sv1 = Student("A", 8.5)
sv2 = Student("B", 12)
sv3 = Student("C", -1)
sv4 = Student("D", 5.5)

print(f"SV1: {sv1.score}, SV2: {sv2.score}, SV3: {sv3.score}, SV4: {sv4.score}")
print("-" * 50)
