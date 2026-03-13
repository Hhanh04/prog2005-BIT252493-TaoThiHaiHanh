def bai5():
    """Bài 5: Xử lý ma trận M x N"""
    print("BÀI 5: MA TRẬN")

    m = int(input("Số hàng M: "))
    n = int(input("Số cột N: "))
    matrix = [[random.randint(0, 99) for _ in range(n)] for _ in range(m)]

    print("\nMa trận:")
    for row in matrix:
        print(row)
    row_idx = int(input("\nHiển thị hàng thứ (0-based): "))
    if 0 <= row_idx < m:
        print(f"Hàng {row_idx}: {matrix[row_idx]}")
    col_idx = int(input("Hiển thị cột thứ (0-based): "))
    if 0 <= col_idx < n:
        col = [matrix[i][col_idx] for i in range(m)]
        print(f"Cột {col_idx}: {col}")
    max_val = max(max(row) for row in matrix)
    print(f"Giá trị lớn nhất: {max_val}")
    print("-" * 50)
