def hitung_jumlah_digit():
    bilangan = int(input("Masukkan bilangan: "))
    jumlah_digit = 0

    while bilangan > 0:
        bilangan = bilangan // 10
        jumlah_digit += 1

    print(f"Jumlah digit: {jumlah_digit}")

# Jalankan fungsi
hitung_jumlah_digit()