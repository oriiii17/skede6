def tampilkan_piramida_angka():
    tinggi = int(input("Masukkan tinggi piramida: "))

    for i in range(1, tinggi + 1):
        # Mencetak spasi
        for j in range(tinggi - i):
            print(" ", end="")
        # Mencetak angka
        for k in range(1, 2 * i):
            print(k, end="")
        print()  # Pindah ke baris baru

# Jalankan fungsi
tampilkan_piramida_angka()