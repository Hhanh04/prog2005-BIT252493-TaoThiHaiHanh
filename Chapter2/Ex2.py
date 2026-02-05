num = int(input("Nhập một số dương: "))
if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} là số nguyên tố.")
    else:
        print(f"{num} không phải là số nguyên tố.")
else:
    print("Số nhập không phải là số nguyên tố (phải lớn hơn 1).")
