# Latihan Caesar Cipher melakukan sebuah pencarian data pada sebuah kamus

# membuat plaintext dengan random huruf alfabet

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# membuat sebuah dictionary dengan data kosongan yang akan menampung sebuah data ketika selesai melakukan pencarian data
ENGLISH_WORDS = []


# membuat function untuk memuat sebuah data yang akan dicari pada sebuah kamus

def get_data():

    dictionary = open("english_words.txt", "r")

    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)

    dictionary.close()

# membuat function untuk menghitung jumlah data yang akan dicari pada sebuah kamus


def count_words(text):
    # upper case letters are needed
    text = text.upper()
    # transform the text into a list of words (split by spaces)
    words = text.split(' ')
    # matches counts the number of english words in the text
    matches = 0

    # consider all the words in the text and check whether the given word is english or not
    for word in words:
        if word in ENGLISH_WORDS:
            matches = matches + 1

    return matches

# memutuskan apakah teks yang dicari itu bahasa inggris atau bukan,ini adalah lanjutan dari function sebelumnya


def is_text_english(text):
    # number of english words in a given text
    matches = count_words(text)

    # you can define your own classification algorithm
    # in this case the assumption: if 70% of the words in the text are english words then
    # it is an english text
    if (float(matches) / len(text.split(' '))) * 100 >= 70:
        return True

    # not an english text
    return False

# membuat function untuk melakukan cracking dengan menggunakan algoritma kriptografi Caesar Chiper


def caesar_crack(cipher_text):
    # we try all the possible key values so the size of the ALPHABET
    for key in range(len(ALPHABET)):

        # reinitialize this to be an empty string
        plain_text = ''

        # we just have to make a simple caesar decryption
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]

        # print the actual decrypted string with the given key
        if is_text_english(plain_text):
            print("We have managed to crack Caesar cipher, the key is: %s, the message is %s" % (
                key, plain_text))


if __name__ == "__main__":
    get_data()
    encrypted = 'VJKUBKUBCBOGUUCIG'
    caesar_crack(encrypted)
