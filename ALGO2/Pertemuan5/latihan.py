nama_karyawan = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (Design/Programmer/Resource): ")
status_perkawinan = input("Masukkan status perkawinan (Y/T): ") 

if jabatan == "Design":
    gaji_pokok = 5000000
elif jabatan == "Programmer":
    gaji_pokok = 10000000
elif jabatan == "Resource":
    gaji_pokok = 5000000
else:
    print("Jabatan tidak valid")

if status_perkawinan == "Y":
    tunjangan_keluarga = 0.2 * gaji_pokok
else:
    tunjangan_keluarga = 0

gaji_kotor = gaji_pokok + tunjangan_keluarga
pajak = 0.1 * gaji_kotor
total_pendapatan = gaji_kotor - pajak


print("Nama karyawan:", nama_karyawan)
print("Jabatan:", jabatan)
print("Gaji pokok:",(f'{gaji_pokok:,.2f}'))
print("Tunjangan keluarga:",(f'{tunjangan_keluarga:,.2f}'))
print("Gaji kotor:", (f'{gaji_kotor:,.2f}'))
print("Pajak:", (f'{pajak:,.2f}'))
print("Total pendapatan setelah pajak:", (f'{total_pendapatan:,.2f}'))
