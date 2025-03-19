def hitung_biaya_parkir():
    jam_parkir = int(input("Masukkan total jam parkir: "))
    if jam_parkir <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (jam_parkir - 2) * 2000
    print(f"Total biaya parkir: {biaya}")

# Jalankan fungsi
hitung_biaya_parkir()