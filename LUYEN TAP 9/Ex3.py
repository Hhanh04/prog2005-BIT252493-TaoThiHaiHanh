# Bài 3:
def bai3():
    print("Bài 3: Chuẩn hóa tên")
    name = input("Nhập tên: ")
    normalized = ' '.join(word.capitalize() for word in name.strip().split())
    print(f"Tên sau chuẩn hóa: {normalized}")
    print("-" * 50)