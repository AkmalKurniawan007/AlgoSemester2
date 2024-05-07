# i = 1
# while i <= 10 :
#     print('Berhitung',i)
#     i += 1

# for i in range(10):
#     if i == 3:
#         continue
#     if i == 7:
#         break
#     print(i)

# total_perulangan = 0
# while True:
#     main = input('Lagi Keluar atau tidak [Ya/Tidak] : ').lower()
#     if main == 'ya':
#         break
#     total_perulangan +=1 
#     print('total perulangan : ',total_perulangan)

while True :
    angka = int(input('masukan angka : '))
    if angka % 2 == 0:
        print(angka,'Bilangan genap')
    else:
        print(angka,'Bilangan Ganjil')