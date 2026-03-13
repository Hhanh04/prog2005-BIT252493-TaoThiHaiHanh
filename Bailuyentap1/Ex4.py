def bai4():
    """Bài 4: In số 1-100, bỏ số chia hết cho 3"""
    print("BÀI 4: SỐ TỪ 1-100 (BỎ CHIA HẾT CHO 3)")
    for i in range(1, 101):
        if i % 3 != 0:
            print(i, end=" ")
    print("\n" + "-" * 50)
