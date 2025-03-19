def tampilkan_segitiga_terbalik():
    tinggi = int(input("Masukkan tinggi segitiga: "))

    for i in range(tinggi, 0, -1):
        # Mencetak spasi
        for j in range(tinggi - i):
            print(" ", end="")
        # Mencetak bintang
        for k in range(2 * i - 1):
            print("*", end="")
        print()  # Pindah ke baris baru

# Jalankan fungsi
tampilkan_segitiga_terbalik()