Jumlah_siswa = int(input("Masukkan jumlah siswa: "))

total_nilai = 0
for i in range(Jumlah_siswa):
    nilai = float(input(f"Masukkan nilai ujian untuk siswa ke-{i+1}: "))
    total_nilai += nilai

average_nilai = total_nilai / Jumlah_siswa

print(f"Rata-rata nilai dari {Jumlah_siswa} siswa adalah: {average_nilai}")

