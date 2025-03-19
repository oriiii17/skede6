def tampilkan_kotak_diagonal():
    ukuran = int(input("Masukkan ukuran kotak: "))

    for i in range(ukuran):
        for j in range(ukuran):
            if i == j or i + j == ukuran - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Pindah ke baris baru

# Jalankan fungsi
tampilkan_kotak_diagonal()