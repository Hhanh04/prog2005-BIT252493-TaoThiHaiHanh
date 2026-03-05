chuoi = input("Nhập một chuỗi: ")
chuoi_clean = chuoi.replace(" ", "").lower()

if chuoi_clean == chuoi_clean[::-1]:
    print(f"'{chuoi}' là chuỗi Palindrome.")
else:
    print(f"'{chuoi}' không phải là chuỗi Palindrome.")
