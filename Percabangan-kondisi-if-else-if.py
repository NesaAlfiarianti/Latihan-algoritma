# Meminta input dari pengguna
hari = input("Masukkan nama hari: ").lower()

# Percabangan kondisi if-elif-else
if hari == "senin":
    print("Hari ini adalah Senin.")
elif hari == "selasa":
    print("Hari ini adalah Selasa.")
elif hari == "rabu":
    print("Hari ini adalah Rabu.")
elif hari == "kamis":
    print("Hari ini adalah Kamis.")
elif hari == "jumat":
    print("Hari ini adalah Jumat.")
elif hari == "sabtu":
    print("Hari ini adalah Sabtu.")
elif hari == "minggu":
    print("Hari ini adalah Minggu.")
else:
    print("Nama hari tidak valid.")