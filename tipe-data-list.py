# Mendefinisikan sebuah list
numbers = [5, 10, 15, 20, 25]

# Menampilkan isi list
print("List angka:", numbers)

# Mengakses angka dalam list
print("angka pertama:", numbers[0])  # Output: 5
print("angka terakhir:", numbers[-1])  # Output: 25

# Mengubah angka dalam list
numbers[2] = 30
print("Setelah mengubah angka ketiga:", numbers)  # Output: [5, 10, 30, 20, 25]

# Menambahkan beberapa angka baru ke list
numbers.extend([35, 40])
print("Setelah menambahkan angka 35 dan 40:", numbers)  # Output: [5, 10, 30, 20, 25, 35, 40]

# Menghapus angka berdasarkan indeks
del numbers[1]  # Menghapus angka kedua
print("Setelah menghapus angka kedua:", numbers)  # Output: [5, 30, 20, 25, 35, 40]

# Mengurutkan list
numbers.sort()
print("Setelah diurutkan:", numbers)  # Output: [5, 20, 25, 30, 35, 40]

# Membalikkan list
numbers.reverse()
print("Setelah dibalik:", numbers)  # Output: [40, 35, 30, 25, 20, 5]