# Pertemuan 02 - Dasar Python dan Pengumpulan GitHub

**Identitas Mahasiswa**
* **Nama**  : Amandita Pebriana Putri
* **NIM**   : 2225250134
* **Kelas** : 3A Pendidikan Matematika

---

## Deskripsi Repositori
Repositori ini berisi latihan dasar pemrograman Python (variabel, tipe data, input-output, operator) serta tugas utama berupa Kalkulator Koordinat Dua Titik.

## Struktur Berkas
* `latihan/01_biodata.py`: Menampilkan biodata terformat dan menghitung umur.
* `latihan/02_persegi_panjang.py`: Menhitung luas dan keliling persegi panjang.
* `latihan/03_konversi_suhu.py`: Mengonversi suhu Celsius ke Fahrenheit dan Kelvin.
* `latihan/04_nilai_akhir.py`: Menhitung nilai akhir berbobot.
* `tugas/kalkulator_koordinat.py`: Menhitung dx, dy, jarak Euclidean, dan titik tengah antara dua titik.

## Cara Menjalankan Program
Jalankan perintah berikut di terminal VS Code:

```bash
python tugas/kalkulator_koordinat.py

## Hasil Pengujian (Test Case Wajib)
| Kasus | Titik A | Titik B | Jarak Euclidean | Titik Tengah | Status |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | (0, 0) | (3, 4) | 5.00 | (1.50, 2.00) | Valid |
| 2 | (-2, 1) | (4, 1) | 6.00 | (1.00, 1.00) | Valid |
| 3 | (2.5, -1) | (2.5, 3) | 4.00 | (2.50, 1.00) | Valid |

## Refleksi
* **Konsep yang paling saya pahami adalah** penggunaan konversi tipe data (`float(input())`) dan pemformatan *f-string* (`{nilai:.2f}`) karena sering dilatih pada bagian materi latihan.
* **Kesalahan yang saya temukan adalah** memahami urutan input angka pada terminal saat program dijalankan dan saya memperbaikinya dengan membaca alur program secara teliti.
* **Pada pertemuan berikutnya saya ingin lebih memahami** penggunaan struktur kondisi (`if-else`) dan fungsi modular pada Python.

## Sumber Referensi
* Modul Bahan Ajar Pertemuan 02 Algoritma dan Pemrograman - Dr. Aan Hendrayana, S.Si., M.Pd.
