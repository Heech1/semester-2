
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

B = [
    [5, 4, 3, 2, 1],
    [10, 9, 8, 7, 6],
    [15, 14, 13, 12, 11],
    [20, 19, 18, 17, 16],
    [25, 24, 23, 22, 21]
]

C = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        total = 0
        for k in range(len(B)):
            total += A[i][k] * B[k][j]
        row.append(total)
    C.append(row)

print("Hasil Perkalian (Matriks C):")
for row in C:
    print(row)

