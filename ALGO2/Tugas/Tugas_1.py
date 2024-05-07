nama = input('Masukan Nama:')
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: ")) 
nilai =  (0.20 * tugas) + (0.30 * uts) +  (0.50 * uas)
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else: 
    grade = 'E'
if nilai > 70:
    status = 'Lulus'
else:
    status = 'Tidak Lulus'

print('Nama:', nama)
print('Nilai Akhir: %0.2f' % nilai)
print('Grade: {}'.format(grade))
print('Status: {}'.format(status))