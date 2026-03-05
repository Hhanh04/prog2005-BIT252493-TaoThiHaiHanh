def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        dong = []
        for j in range(n):
            dong.append(A[i][j] + B[i][j])
        C.append(dong)
    return C
A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8, 9],
    [10, 11, 12]
]

print("Ma trận A:")
for row in A: print(row)
print("Ma trận B:")
for row in B: print(row)

C = cong_ma_tran(A, B)
print("Ma trận C = A + B:")
for row in C: print(row)
