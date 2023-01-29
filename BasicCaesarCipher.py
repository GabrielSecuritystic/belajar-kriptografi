# we need the alphabet because we convert letters into numerical values
# to be able to use mathematical operations (note we encrypt the spaces as well)
# kenapa dikasih spasi karena spasi tersebut digunakan untuk menunjukan index ke.0

"""
Rumus Enkripsi:
key(variable m) + 3 huruf dari plaintext(variable ALPHABET)
misal untuk enkripsi huruf C,harus menggeser 3 huruf ke kanan dari setelah huruf C yaitu huruf F
"""
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

# membuat function untuk melakukan fungsi enkrikpsi


def caesar_encrypt(plain_text):
    # pesan enkripsi kosongan yang akan diisi ketika sudah dilakukan pencocokan sebuah data nantinya
    cipher_text = ''
    # membuat algoritma case sensitive  untuk kombinasi pencocokan data
    plain_text = plain_text.upper()

    # mempertimbangkan semua huruf(huruf alfabet) dalam plaintext
    for c in plain_text:
        # mempertemukan representasi numerik (indeks) yang terkait
        index = ALPHABET.find(c)
        # Caesar cipher merupakan kriptografi yang hanya melakukan sebuah pergeseran sebuah huruf acak yang sudah ditentukan
        # ke kunci menggunakan aritmatika modular untuk mengubah nilai di dalamnya
        # rentang [0,num_of_letters_in_alphabet]
        index = (index + KEY) % len(ALPHABET)
        # tetap menambahkan karakter terenkripsi ke ciphertext
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


# membuat function untuk melakukan fungsi dekripsi
def caesar_decrypt(cipher_text):

    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text


if __name__ == '__main__':

    m = 'Welcome to my Udemy course!'
    encrypted = caesar_encrypt(m)
    print("hasil Enkripsi : ", encrypted)
    print("Hasil Dekripsi : ", caesar_decrypt(encrypted))
