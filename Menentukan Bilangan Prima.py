n = int(input("Masukkan sebuah bilangan: "))
prima = True
if n <= 1:
    prima = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prima = False
            break
if prima:
    print(f"{n} adalah bilangan prima.")
else:
    print(f"{n} bukan bilangan prima.")