def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Input dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Menghitung luas
luas = luas_persegi_panjang(panjang, lebar)

# Menampilkan hasil
print(f"Luas persegi panjang adalah {luas}")
