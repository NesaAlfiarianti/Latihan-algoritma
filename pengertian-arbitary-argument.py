def jumlahkan(*args):
    """
    Fungsi untuk menjumlahkan sejumlah angka.
    
    Parameters:
    *args: Angka yang ingin dijumlahkan.
    
    Returns:
    int: Hasil penjumlahan.
    """
    total = sum(args)  # Menggunakan fungsi sum untuk menjumlahkan semua argumen
    return total

# Menggunakan fungsi dengan berbagai jumlah argumen
print(jumlahkan(1, 2, 3))  # Output: 6
print(jumlahkan(4, 5, 6, 7, 8))  # Output: 30