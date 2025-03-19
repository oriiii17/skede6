hasil = "" 
x = int(input("Masukkan jumlah :")) 
bar = x # Looping Baris 
while bar >= 0: # Looping Kolom Spasi Kosong kol = bar 
    while kol > 0: 
        hasil += " " 
        kol-= 1 # Looping Kolom Bintang 

    kanan = 1 
    while kanan < (x- (bar-1)): 
        hasil += " * " 
        kanan += 1 

    hasil = hasil + "\n" 
    bar-= 1 
        
print (hasil)