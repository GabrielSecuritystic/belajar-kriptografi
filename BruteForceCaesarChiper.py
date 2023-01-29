# latihan membuat program brute force pada algoritma kriptografi Caesar Chiper

"""
Rumus Dekripsi:
chipertext(variable encrypted) - 3 huruf dari plaintext(variable ALPHABET)
misal untuk mendapatkan huruf A,harus menggeser 3 huruf ke kiri dari setelah huruf A yaitu huruf D

Note:
dikarenakan di kasus ini indexnya langsung di hitung dari nol(0) maka pada nilai chipertext yang ada di variable encrypted tdk diberi spasi seperti pada plaintextnya
sehingga rumusnya:
chipertext(variable encrypted) - 2 huruf dari plaintext(variable ALPHABET)
misal untuk mendapatkan huruf A,harus menggeser 2 huruf ke kiri dari setelah huruf A yaitu huruf C
"""
# plaintext
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# membuat function untuk melakukan fungsi crack/bruteforce suatu pesan

def crack_caesar(chipertext):

    for key in range(len(ALPHABET)):
        plaintext = ''

        for c in chipertext:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plaintext = plaintext + ALPHABET[index]

        # menampilkan hasil bruteforce
        print('With key %s, the result is: %s' % (key, plaintext))


if __name__ == '__main__':
    encrypted = 'VJKUBKUBCBOGUUCIG'  # hasilnya THIS IS MESSAGE
    crack_caesar(encrypted)
