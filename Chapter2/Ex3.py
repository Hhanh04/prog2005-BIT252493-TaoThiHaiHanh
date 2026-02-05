n = int(input("Nhập số n: "))
if n <= 0:
    print("n phải là số dương.")
else:
    fib = [0, 1]
    if n == 1:
        print([0])
    elif n == 2:
        print([0, 1])
    else:
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        print(fib)
