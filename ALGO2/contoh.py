Buku = []
judul = str(input("Masukkan Judul : "))
tahun = int(input("Masukkan Tahun : "))
harga = float(input("Masukkan Harga : "))
ketersediaan = bool(input("Masukkan Ketersediaan : "))

data_buku = [judul,tahun,harga,ketersediaan]
Buku.append(data_buku)
print(Buku)