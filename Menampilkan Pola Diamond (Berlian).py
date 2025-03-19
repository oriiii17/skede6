def tampilkan_diamond():
    tinggi = int(input("Masukkan tinggi diamond (harus ganjil): "))

    if tinggi % 2 == 0:
        print("Tinggi harus bilangan ganjil!")
        return

    # Bagian atas diamond
    for i in range(1, tinggi // 2 + 2):
        # Mencetak spasi
        for j in range(tinggi // 2 + 1 - i):
            print(" ", end="")
        # Mencetak bintang
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    # Bagian bawah diamond
    for i in range(tinggi // 2, 0, -1):
        # Mencetak spasi
        for j in range(tinggi // 2 + 1 - i):
            print(" ", end="")
        # Mencetak bintang
        for k in range(2 * i - 1):
            print("*", end="")
        print()

# Jalankan fungsi
tampilkan_diamond()