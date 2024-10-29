# Mendefinisikan sebuah tuple
fruits = ("nesa", "yustin", "ical", "eca")

# Menampilkan isi tuple
print("Tuple orang:", fruits)

# Mengakses orang dalam tuple
print("orang pertama:", fruits[0])  # Output: nesa
print("orang terakhir:", fruits[-1])  # Output: eca

# Menghitung jumlah orang dalam tuple
jumlah_orang = len(fruits)
print("Jumlah orang dalam tuple:", jumlah_orang)  # Output: 4

# Menggunakan orang dalam unpacking
a, b, c, d = fruits
print("orang pertama:", a)  # Output: nesa
print("orang kedua:", b)    # Output: yustin

# Menggabungkan tuple
more_fruits = ("ulpa","athar")
all_fruits = fruits + more_fruits
print("Gabungan tuple:", all_fruits)  # Output: ('nesa', 'yustin', 'ical', 'eca', 'ulpa', 'athar')
