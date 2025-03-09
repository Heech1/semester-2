def hitung_gaji():
    
    nama = input("Masukkan Nama: ")
    nik = input("Masukkan NIK: ")
    status = input("Masukkan Status (Pegawai Tetap/Honor): ").strip().lower()
    golongan = input("Masukkan Golongan (A/B/C): ").strip().upper()
    
    
    gaji = 0
    bonus = 0
    
    
    if status == "pegawai tetap":
        gaji = 1000000
        if golongan == "A":
            bonus = 200000
        elif golongan == "B":
            bonus = 400000
        elif golongan == "C":
            bonus = 550000
        else:
            print("Golongan tidak valid!")
            return
    elif status == "honor":
        gaji = 750000
        if golongan == "A":
            bonus = 150000
        elif golongan == "B":
            bonus = 275000
        elif golongan == "C":
            bonus = 480000
        else:
            print("Golongan tidak valid!")
            return
    else:
        print("Status tidak valid!")
        return
    
    
    gaji_total = gaji + bonus
    
    
    print("\n=== Rincian Gaji ===")
    print("Nama: ",(nama))
    print("NIK: ",(nik))
    print("Status: ",(status.capitalize()))
    print("Golongan: ",(golongan))
    print("Gaji Pokok: Rp {:,}".format(gaji))
    print("Bonus: Rp {:,}".format(bonus))
    print("Total Gaji: Rp {:,}".format(gaji_total))


hitung_gaji()
