# Operator Identitas
# Mendefinisikan variabel
x = 10
y = x            # y merujuk ke objek yang sama dengan x
z = 10           # z adalah nilai yang sama, tapi objek yang berbeda

# Memeriksa identitas
print("Memeriksa identitas:")
print("x is y:", x is y)          # True, karena y adalah referensi yang sama dengan x
print("x is z:", x is z)          # False, karena z adalah objek yang berbeda
print("x is not z:", x is not z)  # True

# Operator Keanggotaan
my_string = "Hello, World!"  # Sebuah string

# Memeriksa keanggotaan
print("\nMemeriksa keanggotaan:")
print("'H' in my_string:", 'H' in my_string)  # True, 'H' ada dalam string
print("'W' in my_string:", 'W' in my_string)  # True, 'W' ada dalam string
print("'x' in my_string:", 'x' in my_string)  # False, 'x' tidak ada dalam string
print("'o' not in my_string:", 'o' not in my_string)  # False, 'o' ada dalam string