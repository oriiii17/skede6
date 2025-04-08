def layout_rumah(panjang_rumah, lebar_rumah, halaman):
    total_panjang = panjang_rumah + 2 * halaman
    total_lebar = lebar_rumah + 2 * halaman
    
    rows = total_panjang + 2
    cols = total_lebar + 2
    
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1:
                print('#', end=' ')
            elif j == 0 or j == cols - 1:
                print('#', end=' ')
            else:
                if (halaman <= i - 1 < halaman + panjang_rumah) and (halaman <= j - 1 < halaman + lebar_rumah):
                    print('R', end=' ')
                else:
                    print('H', end=' ')
        print()


def layout_rumah(panjang_rumah, lebar_rumah, halaman):
    totalpanjang = panjang_rumah + halaman * 2 + 2
    totallebar = lebar_rumah + halaman * 2 + 2
    for i in range(totallebar):
        print("#", end = " ")
        if i == 0 or i == totallebar - 1:
            for j in range (totalpanjang - 1):
                print ("#", end = " ")
        else:
            if i >= 1 and i < totallebar - lebar_rumah - halaman - 1 or i >= lebar_rumah + halaman + 1 and i < totallebar - 1:
                for j in range (totalpanjang - 2):
                    print ("H", end = " ")
                print("#", end = "")
            elif i >= halaman - 1 or i <= lebar_rumah + halaman + 1:
                for j in range (halaman):
                    print("H", end = " ")
                for j in range (panjang_rumah):
                    print ("R", end = " ")
                for j in range (halaman):
                    print("H", end = " ")
                print ("#", end = "")
            else:
                for j in range (totallebar - 2):
                    print (" ", end = " ")
                print("#", end = "")
        print()