def analyze_tuple(numbers):
    """
    Nhận vào tuple các số nguyên và trả về tổng, max, min
    """
    total = sum(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    
    return total, max_val, min_val

# Test
numbers = (1, 5, 3, 9, 2, 8)
tong, lon_nhat, nho_nhat = analyze_tuple(numbers)
print(f"Tuple: {numbers}")
print(f"Tổng: {tong}")
print(f"Giá trị lớn nhất: {lon_nhat}")
print(f"Giá trị nhỏ nhất: {nho_nhat}")
