# def hitung_nilai_akhir(nilai_tugas, nilai_uts,nilai_uas) :
#     bobot_tugas = 0.3
#     bobot_uts = 0.4
#     bobot_uas = 0.4

#     nilai_akhir = (nilai_tugas * bobot_tugas) + (nilai_uts * bobot_uts) + (nilai_uas * bobot_uas)
#     return nilai_akhir

# nilai_tugas = 85
# nilai_uts = 90
# nilai_uas = 80

# nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
# print('Nilai akhir Anda adalah',nilai_akhir)

def cetak_elemen(daftar ) :
    for elemen in daftar :
        print(elemen)

daftar = [1,2,3,4,5]
cetak_elemen(daftar)