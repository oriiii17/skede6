def hitung_total_belanja():
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total = 0
    for i in range(jumlah_barang):
        harga = int(input(f"Masukkan harga barang ke-{i+1}: "))
        total += harga
    print(f"Total belanja: {total}")

# Jalankan fungsi
hitung_total_belanja()