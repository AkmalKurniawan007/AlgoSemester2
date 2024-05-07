
# Fungsi eksekusi operasi matematika
def eksekusi_operasi():
    while True:
        print("Pilih operasi matematika:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '4':
            print("Terima kasih telah menggunakan program.")
            break

        elif pilihan in ['1', '2', '3']:
            # Meminta input dua bilangan dari pengguna
            bilangan1 = float(input("Masukkan bilangan pertama: "))
            bilangan2 = float(input("Masukkan bilangan kedua: "))

            if pilihan == '1':
                hasil = penjumlahan(bilangan1, bilangan2)
                print(f"Hasil penjumlahan: {hasil}")
            elif pilihan == '2':
                hasil = pengurangan(bilangan1, bilangan2)
                print(f"Hasil pengurangan: {hasil}")
            elif pilihan == '3':
                hasil = perkalian(bilangan1, bilangan2)
                print(f"Hasil perkalian: {hasil}")

        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

# Uncomment code below for testing
# eksekusi_operasi()
