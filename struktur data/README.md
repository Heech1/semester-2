# Panduan Penggunaan Program Pencarian Data Google Spreadsheet

Program ini memungkinkan pengguna melakukan pencarian data dari Google Spreadsheet menggunakan metode **Linear Search** dan **Binary Search** berdasarkan:
- Judul Paper
- Tahun Terbit
- Nama Penulis

Namun, untuk alasan keamanan, file `credentials.json` **tidak disertakan** di repositori ini. Kamu perlu membuatnya sendiri agar program bisa dijalankan.

---

## 🔐 Cara Membuat `credentials.json`

1. **Masuk ke Google Cloud Console**
   - Buka: [https://console.cloud.google.com/](https://console.cloud.google.com/)

2. **Buat Project Baru atau Pilih yang Sudah Ada**
   - Klik dropdown project → "New Project"

3. **Aktifkan Google Sheets API dan Google Drive API**
   - Masuk ke menu "APIs & Services > Library"
   - Aktifkan:
     - Google Sheets API
     - Google Drive API

4. **Buat Service Account**
   - Masuk ke menu "IAM & Admin > Service Accounts"
   - Klik "Create Service Account"
   - Masukkan nama → Lanjutkan → Assign Role: "Editor" atau "Viewer"

5. **Buat dan Unduh `credentials.json`**
   - Setelah service account dibuat, klik pada nama akun tersebut
   - Masuk ke tab "Keys" → Add Key → Create New Key → Pilih JSON → Unduh
   - Simpan file tersebut dengan nama: `credentials.json`
   - Letakkan file di satu folder dengan file Python kamu

---

## 📂 Share Spreadsheet ke Service Account

1. Buka file Google Spreadsheet yang akan dipakai
2. Klik tombol "Bagikan (Share)"
3. Masukkan **Client Email** dari file `credentials.json`
   - Contoh: `your-service-account@your-project.iam.gserviceaccount.com`
4. Beri akses sebagai **Editor** atau **Viewer**
5. Untuk dataset yang sesuai pada program dapat diakses disini
https://docs.google.com/spreadsheets/d/17ru4XAU2NloE9Dfxr2PC1BVcsYkLLT5r7nPSsiOFlvQ/edit?gid=743838712#gid=743838712

---

## ▶️ Menjalankan Program

1. Pastikan file `credentials.json` ada di folder yang sama dengan script Python
2. Jalankan program dengan `namafile.py`
3. Pilih metode pencarian dan masukkan keyword

---

Selamat mencoba! 🚀
