import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Struktur_Data_Dataset_Kelas_A_B_C").sheet1

data = sheet.get_all_records()

def binary_search(data, kolom, keyword):
    
    sorted_data = sorted(data, key=lambda x: str(x[kolom]).lower())
    
    low = 0
    high = len(sorted_data) - 1
    hasil = []

    keyword = keyword.lower()

    while low <= high:
        mid = (low + high) // 2
        nilai_tengah = str(sorted_data[mid][kolom]).lower()

        if nilai_tengah == keyword:
            hasil.append(sorted_data[mid])

            # Cari ke kiri
            i = mid - 1
            while i >= 0 and str(sorted_data[i][kolom]).lower() == keyword:
                hasil.insert(0, sorted_data[i])
                i -= 1

            # Cari ke kanan
            i = mid + 1
            while i < len(sorted_data) and str(sorted_data[i][kolom]).lower() == keyword:
                hasil.append(sorted_data[i])
                i += 1
            break
        elif keyword < nilai_tengah:
            high = mid - 1
        else:
            low = mid + 1

    return hasil


print("=== PENCARIAN PAPER (Binary Search) ===")
print("1. Cari berdasarkan Judul")
print("2. Cari berdasarkan Tahun Terbit")
print("3. Cari berdasarkan Nama Penulis")
pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    keyword = input("Masukkan Judul Paper: ")
    hasil = binary_search(data, "Judul Paper", keyword)

elif pilihan == "2":
    keyword = input("Masukkan Tahun Terbit: ")
    hasil = binary_search(data, "Tahun Terbit", keyword)

elif pilihan == "3":
    keyword = input("Masukkan Nama Penulis: ")
    hasil = binary_search(data, "Nama Penulis", keyword)

else:
    print("Pilihan tidak valid.")
    hasil = []


if hasil:
    print("\nHasil ditemukan:\n")
    for i, item in enumerate(hasil, start=1):
        print(f"Data {i}:")
        for k, v in item.items():
            print(f"{k}: {v}")
        print()
else:
    print("\nData tidak ditemukan.")
