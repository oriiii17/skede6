def find_nearest_prime(n):
    # Fungsi untuk mengecek apakah suatu bilangan adalah prima
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Mencari bilangan prima terdekat < n
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return None