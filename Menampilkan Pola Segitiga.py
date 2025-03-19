def tampilkan_pola_segitiga():
    tinggi = int(input("Masukkan tinggi segitiga: "))

    for i in range(1, tinggi + 1):
        # Mencetak spasi
        for j in range(tinggi - i):
            print(" ", end="")
        # Mencetak bintang
        for k in range(2 * i - 1):
            print("*", end="")
        print()

# Jalankan fungsi
tampilkan_pola_segitiga()