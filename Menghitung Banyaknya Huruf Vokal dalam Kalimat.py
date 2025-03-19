def hitung_huruf_vokal():
    kalimat = input("Masukkan kalimat: ").lower()
    vokal = "aiueo"
    count = 0

    for huruf in kalimat:
        if huruf in vokal:
            count += 1

    print(f"Jumlah huruf vokal dalam kalimat: {count}")

# Jalankan fungsi
hitung_huruf_vokal()