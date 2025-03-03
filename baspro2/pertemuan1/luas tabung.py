def luas_tabung(jari_jari, tinggi):
    pi = 3.141592653589793
    luas_selimut = 2 * pi * jari_jari * tinggi
    luas_tutup_dan_alas = 2 * pi * jari_jari ** 2
    return luas_selimut + luas_tutup_dan_alas

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

# Menghitung luas
luas = luas_tabung(jari_jari, tinggi)

# Menampilkan hasil
print(f"Luas permukaan tabung adalah {luas}")
