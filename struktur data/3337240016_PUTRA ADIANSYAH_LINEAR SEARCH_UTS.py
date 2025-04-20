import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Struktur_Data_Dataset_Kelas_A_B_C").sheet1

data = sheet.get_all_records()

def linear_search(data, kolom, keyword):
    hasil = []
    for item in data:
        if str(item[kolom]).lower() == keyword.lower():
            hasil.append(item)
    return hasil

print("=== PENCARIAN PAPER ===")
print("1. Cari berdasarkan Judul")
print("2. Cari berdasarkan Tahun Terbit")
print("3. Cari berdasarkan Nama Penulis")
pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    keyword = input("Masukkan Judul Paper: ")
    hasil = linear_search(data, "Judul Paper", keyword)
elif pilihan == "2":
    keyword = input("Masukkan Tahun Terbit: ")
    hasil = linear_search(data, "Tahun Terbit", keyword)
elif pilihan == "3":
    keyword = input("Masukkan Nama Penulis: ")
    hasil = linear_search(data, "Nama Penulis", keyword)
else:
    print("Pilihan tidak valid.")
    hasil = []

if hasil:
    print("\nHasil ditemukan:")
    for i, h in enumerate(hasil, 1):
        print(f"\nData {i}:")
        for k, v in h.items():
            print(f"{k}: {v}")
else:
    print("Data tidak ditemukan.")
