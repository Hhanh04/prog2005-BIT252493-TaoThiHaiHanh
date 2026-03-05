def count_vowels(s):
    vowels = "aeiouAEIOU"
    dem = 0
    for char in s:
        if char in vowels:
            dem += 1
    return dem

chuoi = input("Nhập chuỗi: ")
kq = count_vowels(chuoi)
print(f"Số lượng nguyên âm: {kq}")
