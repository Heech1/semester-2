def luas_lingkaran(jari_jari):
    pi = 3.141592653589793
    return pi * jari_jari ** 2

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas
luas = luas_lingkaran(jari_jari)

# Menampilkan hasil
print(f"Luas lingkaran adalah {luas}")