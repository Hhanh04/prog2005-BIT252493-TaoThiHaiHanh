def bai10():
    """Bài 10: Quản lý sản phẩm với file"""
    print("BÀI 10: QUẢN LÝ SẢN PHẨM")
    FILENAME = "products.txt"

    while True:
        print("\n1. Thêm sản phẩm")
        print("2. Hiển thị danh sách")
        print("3. Sắp xếp theo giá giảm dần")
        print("4. Thoát")

        choice = input("Chọn (1-4): ")

        if choice == "1":
            code = input("Mã SP: ")
            name = input("Tên SP: ")
            price = float(input("Giá: "))
            with open(FILENAME, 'a', encoding='utf-8') as f:
                f.write(f"{code};{name};{price}\n")
            print("Đã thêm!")

        elif choice == "2":
            if os.path.exists(FILENAME):
                products = []
                with open(FILENAME, 'r', encoding='utf-8') as f:
                    for line in f:
                        parts = line.strip().split(';')
                        if len(parts) == 3:
                            products.append({
                                'code': parts[0],
                                'name': parts[1],
                                'price': float(parts[2])
                            })

                print("\nDANH SÁCH SẢN PHẨM:")
                for p in products:
                    print(f"{p['code']} - {p['name']} - {p['price']}")
            else:
                print("File chưa có dữ liệu!")

        elif choice == "3":
            if os.path.exists(FILENAME):
                products = []
                with open(FILENAME, 'r', encoding='utf-8') as f:
                    for line in f:
                        parts = line.strip().split(';')
                        if len(parts) == 3:
                            products.append({
                                'code': parts[0],
                                'name': parts[1],
                                'price': float(parts[2])
                            })

                sorted_products = sorted(products, key=lambda x: x['price'], reverse=True)

                print("\nSẮP XẾP GIÁ GIẢM DẦN:")
                for p in sorted_products:
                    print(f"{p['code']} - {p['name']} - {p['price']}")
            else:
                print("File chưa có dữ liệu!")

        elif choice == "4":
            break
