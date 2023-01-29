from hashlib import sha256

"""
Output yang dihasilkan panjangnya 256 bits
hasilnya adalah urutan heksadesimal sepanjang 64 karakter
1 karakter heksadesimal ukurannya 4 bits
"""
s1 = 'hello world'
s2 = 'halo dunia'

result1 = sha256(s1.encode())
result2 = sha256(s2.encode())

print(result1.hexdigest())
print(result2.hexdigest())
