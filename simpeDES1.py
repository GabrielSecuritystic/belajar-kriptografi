from Crypto.Cipher import DES
from secrets import token_bytes


"""
Rumus Encrypt DES:
Li = Ri-1
Ri=Li-1 XOR f(Ri-1,Ki)

Ketrangan:
Li = adalah sebuah block kode yang ada di sisi  kiri dengan sejumlah i atau data yang ada
Ri = adalah sebuah block kode yang ada di sisi kanan dengan sejumlah i atau data yang ada
f = adalah sebuah fungsi yang menggambarkan proses transformasi encrypt DES

Proses
1.Pertama Blok plaintext dipermutasi dengan matriks permutasi awal(initial permutation atau IP)
2.Kemudianhasil permutasi awal di enchipering sebanyak 16 kali(16 putaran).Setiap 16 putaran menggunakankunci internal yang berbeda
3.Setelah itu hasil enciphering kemudina dipermutasi dengan matrikspermutasi balikan(invers initial permutation atau IP invers) menjadi blok chiperteks.

Rumus Decrypt DES:
Ri - 1 =Li
Li-1 =Ri XOR f(Ri-1,Ki)=Ri XOR f(Li,Ki)

Proses:
Jika pada proses enkripsi urutan kunci internal yang digunakan adalah Ki,K2,K3...sampai K16,
maka pada proses Decrypt urutan kunci yang digunakan adalah K16,K15,...sampai K1
"""
key = token_bytes(8)


def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('utf-8')
    except:
        return False


nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)

print(f'Cipher text: {ciphertext}')

if not plaintext:
    print('Message is corrupted!')
else:
    print(f'Plain text: {plaintext}')
