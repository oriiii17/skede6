def tampilkan_kotak_kondisi():
    n = int(input("Masukkan ukuran kotak: "))

    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                print("*", end=" ")
            elif i % 2 == 0 or j % 2 == 0:
                print("-", end=" ")
            else:
                print("+", end=" ")
        print()  # Pindah ke baris baru

# Jalankan fungsi
tampilkan_kotak_kondisi()