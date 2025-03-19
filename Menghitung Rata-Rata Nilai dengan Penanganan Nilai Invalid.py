def hitung_rata_rata():
    jumlah_nilai = int(input("Masukkan jumlah nilai: "))
    total = 0
    count = 0

    for i in range(jumlah_nilai):
        nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
        if 0 <= nilai <= 100:
            total += nilai
            count += 1
        else:
            print(f"Nilai {nilai} invalid dan tidak dihitung.")

    if count > 0:
        rata_rata = total / count
        print(f"Rata-rata nilai: {rata_rata:.2f}")
    else:
        print("Tidak ada nilai valid yang dimasukkan.")

# Jalankan fungsi
hitung_rata_rata()