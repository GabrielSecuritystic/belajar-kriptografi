from hashlib import sha512

"""
Output yang dihasilkan panjangnya 512 bits
hasilnya adalah urutan heksadesimal sepanjang 128 karakter
1 karakter heksadesimal ukurannya 4bits
jumlah hash yang dihasilkan sebanyak=2^512 (2 pangkat 512)
jumlah hash ini dua kali lebih besar dibanding sha256 yang menghasilkan 2^256
"""
s1 = 'Hello world!'
s2 = 'Hello world'

result1 = sha512(s1.encode())
result2 = sha512(s2.encode())

print(result1.hexdigest())
print(result2.hexdigest())
