def hitung_gaji():
    gaji_pokok = int(input("Masukkan gaji pokok per jam: "))
    jam_kerja = int(input("Masukkan total jam kerja: "))
    
    if jam_kerja > 40:
        lembur = (jam_kerja - 40) * (gaji_pokok * 1.5)
        total_gaji = (40 * gaji_pokok) + lembur
    else:
        total_gaji = jam_kerja * gaji_pokok
    print(f"Total gaji: {total_gaji}")

# Jalankan fungsi
hitung_gaji()