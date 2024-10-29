# Menggunakan loop while untuk meminta input pengguna hingga 'nesa' dimasukkan
while True:  # Loop tak terbatas
    nama = input("nama saya adalah nesa): ")
    if nama.lower() == 'nesa':  # Memeriksa jika pengguna mengetik 'nesa'
        print("Program dihentikan.")
        break  # Menghentikan loop
    else:
        print("Halo,", nama)  # Menyapa pengguna