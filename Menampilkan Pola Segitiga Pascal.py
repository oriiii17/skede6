def tampilkan_segitiga_pascal():
    tinggi = int(input("Masukkan tinggi segitiga Pascal: "))

    for i in range(tinggi):
        # Mencetak spasi
        for j in range(tinggi - i - 1):
            print(" ", end="")
        # Menghitung dan mencetak nilai
        nilai = 1
        for k in range(i + 1):
            print(nilai, end=" ")
            nilai = nilai * (i - k) // (k + 1)
        print()  # Pindah ke baris baru

# Jalankan fungsi
tampilkan_segitiga_pascal()