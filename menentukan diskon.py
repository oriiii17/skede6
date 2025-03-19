def hitung_diskon():
    total_belanja = int(input("Masukkan total belanja: "))
    if total_belanja > 100000:
        diskon = total_belanja * 0.10
        total_bayar = total_belanja - diskon
    else:
        total_bayar = total_belanja
    print(f"Total pembayaran setelah diskon: {total_bayar}")

# Jalankan fungsi
hitung_diskon()