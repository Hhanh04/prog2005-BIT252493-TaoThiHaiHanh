# Bài 1:
def bai1():
    print("Bài 1: Tính BMI")
    weight = float(input("Nhập cân nặng (kg): "))
    height = float(input("Nhập chiều cao (m): "))
    bmi = weight / (height * height)
    print(f"BMI = {bmi:.2f}")
    print("-" * 50)