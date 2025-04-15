
# Matrix Multiplication 5x5 in Python

## 📥 Input

Program ini melakukan perkalian dua buah matriks berukuran 5x5, yaitu:

### Matriks A:
```
[1,  2,  3,  4,  5]
[6,  7,  8,  9, 10]
[11, 12, 13, 14, 15]
[16, 17, 18, 19, 20]
[21, 22, 23, 24, 25]
```

### Matriks B:
```
[5,  4,  3,  2,  1]
[10, 9,  8,  7,  6]
[15, 14, 13, 12, 11]
[20, 19, 18, 17, 16]
[25, 24, 23, 22, 21]
```

## ⚙️ Proses Perkalian Matriks

Perkalian matriks dilakukan dengan rumus:

```
C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + A[i][2]*B[2][j] + A[i][3]*B[3][j] + A[i][4]*B[4][j]
```

Program Python menggunakan tiga nested loop untuk menghitung hasil dari baris ke-i matriks `A` dikalikan dengan kolom ke-j matriks `B`.

### Potongan Kode:
```python
C = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        total = 0
        for k in range(len(B)):
            total += A[i][k] * B[k][j]
        row.append(total)
    C.append(row)
```

## 📤 Output

Hasil dari perkalian matriks `A × B` adalah:

```
[ 275,  260,  245,  230,  215]
[ 650,  610,  570,  530,  490]
[1025,  960,  895,  830,  765]
[1400, 1310, 1220, 1130, 1040]
[1775, 1660, 1545, 1430, 1315]
```

