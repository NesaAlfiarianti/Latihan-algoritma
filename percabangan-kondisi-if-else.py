# Meminta input dari pengguna
nilai = int(input("Masukkan nilai (0-100): "))
# Percabangan kondisi if-else
if nilai >= 80:
    print("Anda mendapatkan nilai A.")
elif nilai >= 70:
    print("Anda mendapatkan nilai B.")
elif nilai >= 60:
    print("Anda mendapatkan nilai C.")
elif nilai >= 50:
    print("Anda mendapatkan nilai D.")
else:
    print("Anda mendapatkan nilai F.")