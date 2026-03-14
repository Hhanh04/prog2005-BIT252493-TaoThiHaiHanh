def kiem_tra_key(dictionary, key):
    """
    Kiểm tra key có tồn tại trong dictionary không
    """
    if key in dictionary:
        print(f"Key '{key}' TỒN TẠI trong dictionary")
        print(f"Giá trị: {dictionary[key]}")
    else:
        print(f"Key '{key}' KHÔNG tồn tại trong dictionary")

# Test
my_dict = {"name": "Nhy Y", "age": 18, "city": "Hoa Thanh Que"}

kiem_tra_key(my_dict, "name")   # Tồn tại
kiem_tra_key(my_dict, "phone")  # Không tồn tại
