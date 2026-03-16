# Bài 4:
def bai4():
    print("Bài 4: Xử lý chuỗi")
    s = input("Nhập chuỗi: ")

    uppercase = sum(1 for c in s if c.isupper())
    lowercase = sum(1 for c in s if c.islower())
    digits = sum(1 for c in s if c.isdigit())
    spaces = sum(1 for c in s if c.isspace())
    special = len(s) - (uppercase + lowercase + digits + spaces)

    vowels = sum(1 for c in s.lower() if c in 'aeiou')
    consonants = lowercase - vowels

    print(f"Số chữ in hoa: {uppercase}")
    print(f"Số chữ in thường: {lowercase}")
    print(f"Số chữ số: {digits}")
    print(f"Số ký tự đặc biệt: {special}")
    print(f"Số khoảng trắng: {spaces}")
    print(f"Số nguyên âm: {vowels}")
    print(f"Số phụ âm: {consonants}")
    print("-" * 50)