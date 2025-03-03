# rumus
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Input dari pengguna
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Menghitung luas
luas = luas_segitiga(alas, tinggi)

# Menampilkan hasil
print(f"Luas segitiga adalah {luas}")
