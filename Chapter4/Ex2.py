def tinh_diem_trung_binh(students_dict):
    """
    Tính điểm trung bình của các sinh viên
    """
    if not students_dict:
        return 0

    total_score = sum(students_dict.values())
    avg_score = total_score / len(students_dict)
    return avg_score


# Tạo dictionary
sinh_vien = {
    "Le Thi Nhu Y": 9.5,
    "Nguyen Minh Huyen": 9.2,
    "Nguyen Thi Thao Linh": 9.0
}

# Test
diem_tb = tinh_diem_trung_binh(sinh_vien)
print("Dictionary sinh viên:", sinh_vien)
print(f"Điểm trung bình: {diem_tb:.2f}")
