# implementasi Kriptografi algoritma VigenereCipher


"""
Rumus algoritma VigenereCipher
-.Enkripsi
C = (p+k) mod 26
keterangan:
C adalah Ciphertext
p adalah plaintext
k adalah key atau kunci
mod adalah modulus atau sisa hasil bagi

-.Dekripsi
p = (c-k) mod 26

Catatan:
Jika panjang kunci atau key lebih pendek daripada panjang plaintext,
maka kunci atau key diulang dari awal dalam penggunaannya(secara periodik)
"""
# plaintext
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigener_encrypt(plaintext, key):

    # proses encrypt pada sebuah text/plaintext(variable ALPHABET)

    plaintext = plaintext.upper()  # membuat sebuah plaintext menjadi huruf kapital semua
    key = key.upper()  # membuat sebuah key menjadi huruf kapital semua

    # membuat sebuah cipher text kosongan yang nantinya akan diisi hasil dari encrypt plaintext diatas
    ciphertext = ''
    key_index = 0

    # membuat looping yang akan digunakan untuk mencocokan semua data
    for character in plaintext:

        index = (ALPHABET.find(character) +
                 ALPHABET.find(key[key_index])) % len(ALPHABET)
        # menambahkan sebuah karakter yang telah di encrypt ke dalam sebuah ciphertext
        ciphertext = ciphertext + ALPHABET[index]

        # melakukan penambahan atau increment pada kunci/key yang akan dimuat pada karakter selanjutnya dimana setiap chipertext yang muncul karakternya berbeda beda
        key_index = key_index + 1

        # membuat pengkondisian jika karakter yang dicari sudah limit/dibatas akhir maka akan mengulangi lagi
        if key_index == len(key):
            key_index = 0
    # mengembalikan atau mengulangi nilai dari ciphher text ynag dihasilkan
    return ciphertext


# membuat function untuk melakukan decrypt
def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ''
    key_index = 0

    for character in ciphertext:
        index = (ALPHABET.find(character) -
                 ALPHABET.find(key[key_index])) % len(ALPHABET)
        plaintext = plaintext + ALPHABET[index]

        key_index = key_index + 1

        if key_index == len(key):
            key_index = 0

    return plaintext

# menjalankan skrip yang sudah dibuat diatas dan tidak bisa di eksport sebagai sebuah module


if __name__ == '__main__':
    text = "CRYPTOGRAPHY"
    cipher = vigener_encrypt(text, 'CRYPTO')
    # mencetak hasil decrypt sebuah chipertext dan key yang diberikan diatas
    print(vigenere_decrypt(cipher, 'CRYPTOGRAPHY'))
