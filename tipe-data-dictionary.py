 # Membuat dictionary
data_mahasiswa = {
    "nama": "nesa",
    "umur": 17,
    "jurusan": "sistem informasi"
}

# Mengakses nilai
print(data_mahasiswa["nama"])  # Output: nesa
print(data_mahasiswa["umur"])   # Output: 17

# Menambahkan pasangan kunci-nilai baru
data_mahasiswa["universitas"] = "Universitas sulawesi barat"

# Menghapus pasangan kunci-nilai
del data_mahasiswa["umur"]

# Menampilkan seluruh dictionary
print(data_mahasiswa)

