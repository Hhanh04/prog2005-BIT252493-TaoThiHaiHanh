class Student:
    def __init__(self, name, score):
        self.name = name
        if 0 <= score <= 10:
            self.score = score
        else:
            self.score = 0

    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")

print("BÀI 9 - PHƯƠNG THỨC DISPLAY():")
sv1 = Student("Lee Thị Như Ý", 8.5)
sv2 = Student("Nguyễn Thị Minh Hy", 11)

sv1.display()
sv2.display()
print("-" * 50)
