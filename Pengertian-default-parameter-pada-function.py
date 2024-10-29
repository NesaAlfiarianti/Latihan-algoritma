def sapa(nama, salam="hai"):
    """Fungsi untuk menyapa seseorang dengan salam yang diberikan."""
    return f"{salam}, {nama}!"

# Memanggil fungsi dengan kedua argumen
print(sapa("nesa", "halo"))  # Output: helo, nesa!

# Memanggil fungsi hanya dengan nama, menggunakan default parameter untuk salam
print(sapa("ical"))  # Output: hai, ical!