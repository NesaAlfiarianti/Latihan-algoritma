def cetak_data(**kwargs):
    """
    Fungsi untuk mencetak informasi yang diberikan melalui keyword arguments.
    
    Parameters:
    **kwargs: Informasi yang ingin ditampilkan.
    
    Returns:
    None
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Menggunakan fungsi dengan keyword arguments
cetak_data(nama="zall", usia=17, kota="majene")
# Output:
# nama: zall
# usia: 17
# kota: majene

# Menggunakan lebih banyak data
cetak_data(motor="vario", warna="hitam", tahun=2024)
# Output:
# mobil: vario
# warna: hitam
# tahun: 2024