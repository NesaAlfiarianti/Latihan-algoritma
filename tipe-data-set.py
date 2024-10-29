# Mendefinisikan sebuah set
colors = {"merah", "hijau", "biru"}

# Menampilkan isi set
print("Set warna:", colors)

# Menambahkan beberapa elemen ke set
colors.update({"kuning", "ungu"})
print("Set setelah menambahkan kuning dan ungu:", colors)

# Menghapus elemen dari set
colors.discard("biru")  # Menggunakan discard untuk menghindari error jika elemen tidak ada
print("Set setelah menghapus biru:", colors)

# Memeriksa apakah elemen ada dalam set
if "merah" in colors:
    print("Merah ada dalam set.")
else:
    print("Merah tidak ada dalam set.")

# Menghitung jumlah elemen dalam set
jumlah_warna = len(colors)
print("Jumlah warna dalam set:", jumlah_warna)  # Output: Jumlah warna dalam set: 4

# Menggunakan set untuk operasi difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Difference
difference_set = set1 - set2
print("Elemen di set1 tetapi tidak di set2:", difference_set)  # Output: {1, 2}

# Symmetric difference
symmetric_difference_set = set1 ^ set2
print("Elemen yang hanya ada di salah satu set:", symmetric_difference_set)  # Output: {1, 2, 5, 6}

# Mengonversi list menjadi set untuk menghilangkan duplikat
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Angka unik dari list:", unique_numbers)  # Output: {1, 2, 3, 4, 5}
