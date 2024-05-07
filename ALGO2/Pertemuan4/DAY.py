nama = input("Masukkan nama : ")
umur = int(input("Masukkan umur : "))
pekerjaan_orang_tua = input("Masukkan pekerjaan orang tua : ")
gaji_orang_tua = int(input("Masukkan gaji orang tua : "))
ipk = float(input("Masukkan IPK: "))


syarat_pekerjaan = ["Dosen", "PNS", "Dokter", "TNI"]  
maksimal_gaji = 1000000  
min_ipk = 2.7  
max_umur = 25  


if pekerjaan_orang_tua not in syarat_pekerjaan and gaji_orang_tua <= maksimal_gaji and ipk >= min_ipk and umur < max_umur:
    print("=========================================")
    print("  SELAMAT KAMU MENDAPTKAN BEASISWA.....!!!")
    print("Nama :", nama)
    print("Umur :", umur)
    print("Pekerjaan orang tua :", pekerjaan_orang_tua)
    print("Gaji orang tua :", gaji_orang_tua)
    print("IPK :", ipk)
    print("Hasil: Siswa memenuhi syarat untuk mendapatkan beasiswa.")
else:
    print("Maaf,", nama, "Tidak memenuhi syarat untuk mendapatkan beasiswa.")
    print(" JANGAN MENYERAH DAN TERUS SEMANGGAT")

