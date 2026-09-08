# Latihan 4: Nilai Akhir
BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

nama = input("Nama Mahasiswa: ")
nilai_tugas = float(input("Nilai Tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

nilai_akhir = (nilai_tugas * BOBOT_TUGAS) + (nilai_uts * BOBOT_UTS) + (nilai_uas * BOBOT_UAS)

print(f"\nNilai Akhir ({nama}): {nilai_akhir:.2f}")