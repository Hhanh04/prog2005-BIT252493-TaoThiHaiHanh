a = []
for i in range(5):
    a.append(input("Nhập chuỗi: "))

for i in range(5):
    for j in range(4-i):
        if len(a[j]) < len(a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
            print(a)

print("Kết quả:", a)