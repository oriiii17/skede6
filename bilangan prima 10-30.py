def tampilkan_bilangan_prima():
    def is_prima(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    start = int(input("Masukkan awal rentang: "))
    end = int(input("Masukkan akhir rentang: "))

    print(f"Bilangan prima antara {start} dan {end}:")
    for num in range(start, end + 1):
        if is_prima(num):
            print(num, end=" ")

# Jalankan fungsi
tampilkan_bilangan_prima()