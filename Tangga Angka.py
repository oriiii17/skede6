def tanggaAngka(n):
    try :
        if n > 0 :
            for i in range(1, n + 1):
                for j in range(1, i+1):
                    print(j,end=" ")
                for k in range(j, 0, -1):
                    print(k, end=" ")
                print()
        elif n < 0 :
            for i in range(n, 0, +1):
                for j in range(-1, i-1, -1):
                    print(j, end=" ")
                for k in range(j, 0, +1):
                    print(k ,end=" ")
                print()
        elif n == 0 :
            print("n tidak valid!")
    except :
        print("n tidak valid!")