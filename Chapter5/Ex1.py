import matplotlib.pyplot as plt
categories = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]
plt.bar(categories, values)
plt.title("Kết quả học tập của lớp")
plt.xlabel("Mức độ")
plt.ylabel("Số học sinh")
plt.show()