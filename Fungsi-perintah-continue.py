 # Menggunakan loop for untuk mencetak angka ganjil dari 1 hingga 20
for angka in range(1, 21):  # Loop dari 1 hingga 20
    # Memeriksa apakah angka genap
    if angka % 2 == 0:  
        continue  # Melewatkan iterasi ini jika angka genap
    # Mencetak angka ganjil
    print("Angka ganjil:", angka)  

print("Loop selesai.")