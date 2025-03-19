def generate_matrix(tinggi, lebar):
    angka = 1  # Mulai dari angka 1
    for i in range(tinggi):
        for j in range(lebar):
            print(angka, end=" ")  # Cetak angka dan spasi
            angka += 1  # Increment angka
        print()  # Pindah ke baris baru setelah satu baris selesai

# Input dari pengguna
tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

# Menampilkan deret dalam bentuk matriks
generate_matrix(tinggi, lebar)