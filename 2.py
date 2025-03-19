def generate_sequence(n):
    # Fungsi untuk menghitung faktorial
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    # Menghasilkan deret sesuai pola
    for i in range(n, 0, -1):
        # Cetak faktorial dari i
        print(factorial(i), end=" ")
        
        # Cetak deret angka dari i hingga 1
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()  # Pindah ke baris baru