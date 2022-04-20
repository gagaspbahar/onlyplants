# IF2250-2022-K01-11-OnlyPlants

> **OnlyPlants** merupakan layanan peminjaman tanaman yang berbasis aplikasi sehingga dapat digunakan dimana saja, dan kapan saja. Aplikasi ini memperbolehkan pengguna untuk memilih jumlah tanaman yang ingin disewa, tanggal mulai sewa, dan tanggal pengembelian. Tanpa banyak basa-basi, **Selamat Mencoba!**

## Cara Instalasi
---

1. Unduh repository ke penyimpanan lokal dengan membuka cmd dan mengetik
```
git clone https://gitlab.informatika.org/gagaspbahar/if2250-2022-k01-11-onlyplants.git
```
2. Unduh semua requirements dengan membuka repository dan mengetik
```
pip install -r requirements.txt
```
## Cara Penggunaan
1. Buka terminal pada repository penyimpanan ini (**if2250-2022-k01-11-onlyplants**)
2. Ketik
```
python src/main.py
```
3. Selamat bermain dengan aplikasi buatan kami! Saran dan masukan sangat kami harapkan.

## Daftar Modul
---
| Modul | Nama | NIM |
| ---  | --- | --- |
| Login & Registrasi |Gagas Praharsa Bahar  | 13520016 
| Melihat Tanaman |Andhika Arta Aryanto | 13520081
| Input & Edit Tanaman |Rania Dwi Fadhilah | 13520142
| Memilih Tanaman & Checkout | Angelica Winasta Sinisuka | 13520097

## Daftar Tabel Basis Data
---

### 1. Tabel **Akun_User**
| Atribut | Jenis |
| ---  | --- | 
| idAkun | int
| customerName | varchar(225)
| email | varchar(225)
| username | varchar(30)
| passwordHash | varbinary(50)
| noTelp | varchar(15)
| address | varchar(300)
| postalCode | int

### 2. Tabel **Tanaman**
| Atribut | Jenis |
| ---  | --- | 
| idTanaman | int
| nama | varchar(50)
| harga | double
| stok | int
| deskripsi | text
| image | blob
| asal_kota | varchar(50)

### 3. Tabel **Pemesanan**
| Atribut | Jenis |
| ---  | --- | 
| orderNumber | int
| idPelanggan | int
| tanggalPemesanan | dateTime

### 4. Tabel **Detail_Pemesanan**
| Atribut | Jenis |
| ---  | --- | 
| orderNumberDetail | int
| orderNumber | int
| idTanaman | int
| kuantitas | int
| from_date | date
| until_date | date
| status_penyewaan | varchar(50)
| price | double

## Status Projek
---
Belum selesai
