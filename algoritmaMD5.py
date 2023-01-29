from hashlib import md5

"""
Ukuran message digest 128 bits
Rumus encode:
32 hexadecimal karakter - ukuran message digest yaitu 128bits

yang mana setiap block memiliki ukuran 32bits

"""
s = "contoh algoritma  hashing md5"

print("plaintext: ", s)
result = md5(s.encode())

# mencetak hasil hasil encode dari suatu plainttext
print("hasil encode: ", result.hexdigest())
