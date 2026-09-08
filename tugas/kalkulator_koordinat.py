"""
Tugas Utama: Kalkulator Koordinat Dua Titik
Nama  : Amandita Pebriana Putri
NIM   : 2225250134
Kelas : Pendidikan Matematika
 Deskripsi: Program untuk menghitung perubahan koordinat (dx, dy),
            jarak Euclidean, dan titik tengah antara dua titik A dan B.
"""

print("========================================")
print("    KALKULATOR KOORDINAT DUA TITIK     ")
print("========================================\n")

# 1. Input Koordinat
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

# 2. Proses Perhitungan
dx = x2 - x1
dy = y2 - y1

# Jarak Euclidean: akar kuadrat dari (dx^2 + dy^2)
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# Titik Tengah
titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

# 3. Output Hasil
print("\n----------------------------------------")
print(f"Titik A       : ({x1:.2f}, {y1:.2f})")
print(f"Titik B       : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan     : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B  : {jarak:.2f}")
print(f"Titik tengah  : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")
print("----------------------------------------")
