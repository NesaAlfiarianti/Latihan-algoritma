# Menggunakan loop for dengan enumerate untuk mencetak indeks dan nilai
daftar = ["apel", "pisang", "ceri"]

for indeks, buah in enumerate(daftar):  # Mendapatkan indeks dan elemen
    print(f"Indeks {indeks}: {buah}")

print("Loop selesai.")