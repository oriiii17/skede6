def tampilkan_kotak_berangka():
    ukuran = int(input("Masukkan ukuran kotak: "))

    for i in range(ukuran):
        for j in range(ukuran):
            print((i + j) % ukuran + 1, end=" ")
        print()  # Pindah ke baris baru

# Jalankan fungsi
tampilkan_kotak_berangka()