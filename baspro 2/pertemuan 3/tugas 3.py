def hitung_gaji():
    nama = input("Masukkan Nama: ")
    nik = input("Masukkan NIK: ")
    
    status_list = ["pegawai tetap", "honor"]
    golongan_list = ["A", "B", "C"]
    
    status = ""
    golongan = ""
    
    for i in status_list:
        statusInput = input("Masukkan Status (Pegawai Tetap/Honor): ").strip().lower()
        if statusInput == "pegawai tetap" or statusInput == "honor":
            status = statusInput
            break
        print("Status tidak valid! Masukkan 'Pegawai Tetap' atau 'Honor'.")
    else:
        print("Terlalu banyak percobaan. Program dihentikan.")
        return
    
    for j in golongan_list:
        golonganInput = input("Masukkan Golongan (A/B/C): ").strip().upper()
        if golonganInput in golongan_list:
            golongan = golonganInput
            break
        print("Golongan tidak valid! Masukkan A, B, atau C.")
    else:
        print("Terlalu banyak percobaan. Program dihentikan.")
        return
    
    gaji = 0
    bonus = 0
    
    for i in status_list:
        if status == "pegawai tetap":
            gaji = 1000000
            for j in golongan_list:
                if golongan == "A":
                    bonus = 200000
                elif golongan == "B":
                    bonus = 400000
                elif golongan == "C":
                    bonus = 550000
            break
        elif status == "honor":
            gaji = 750000
            for j in golongan_list:
                if golongan == "A":
                    bonus = 150000
                elif golongan == "B":
                    bonus = 275000
                elif golongan == "C":
                    bonus = 480000
            break
    
    gaji_total = gaji + bonus
    
    print("\n=== Rincian Gaji ===")
    print("Nama: ", nama)
    print("NIK: ", nik)
    print("Status: ", status.capitalize())
    print("Golongan: ", golongan)
    print("Gaji Pokok: Rp {:,}".format(gaji))
    print("Bonus: Rp {:,}".format(bonus))
    print("Total Gaji: Rp {:,}".format(gaji_total))

hitung_gaji()

