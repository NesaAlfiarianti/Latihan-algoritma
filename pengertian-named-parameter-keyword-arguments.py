def sapa(nama, salam="Hai"):
    """
    Fungsi untuk menyapa seseorang.
    
    Parameters:
    nama (str): Nama orang yang disapa.
    salam (str): Salam yang digunakan (default: "Halo").
    
    Returns:
    str: Pesan sapaan.
    """
    return f"{salam}, {nama}!"

# Menggunakan keyword arguments
print(sapa(nama="nesa"))  # Output: Halo, nesa!
print(sapa(nama="zal", salam="hai"))  # Output: hai, zal!