from Crypto.Cipher import DES
import binascii

# we can use the DES algorithm like this - there are several modes (7 modes)
#
# 1.) ECB: "Electronic Code Book" -> we use DES on every 64 bits long plaintext block
#     these blocks are independent of each other so we use DES separately on every block
#        The problem is that it is vulnerable: identical plain texts with identical keys
#          encrypt to identical cipher texts and two plain texts with partial
#           identical portions encrypted with the same key will have partial identical
#               cipher text portions
#
# 2.) CBC: "Cipher Block Chaining" -> (XOR) uses a chaining mechanism that causes
#           the decryption of a block of cipher text to depend on all the
#                   preceding cipher text blocks
#
#  THE PADDING PROBLEM
#     DES algorithm uses 64 bits long inputs: what if the plaintext is not divisible by 64?
#        ~ in these cases we append some extra bits to the plaintext to be able to split
#              the plaintext into 64 bits long chunks
#
#     Padding modes:
#        -> we can add extra bits: 100000 for example
#        -> we can add white-spaces to the plaintext
#        -> we can use CMS "Cryptographic Message Syntax"
#                   (or the Public Key Cryptography Standards)
#                pad with bytes all of the same value as the number of padding bytes
#
#                            1 padding byte needed: 0x01
#                            2 padding bytes needed: 0x02
#                            3 padding byte needed: 0x03
#                            4 padding byte needed: 0x04
#
# for example we have the plaintext containing 18 bytes:
# F14ADBDA019D6DB7 EFD91546E3FF8444 9BCB then we must add 14
# bytes as padding (that has the hex value 0x0E) so the transformed plain text is:
#  F14ADBDA019D6DB7 EFD91546E3FF8444 9BCB0E0E0E0E0E0E 0E0E0E0E0E0E0E0E


def add_padding(text, blocksize=64):
    pad_len = blocksize - (len(text) % blocksize)
    padding = '$' * pad_len
    return text + padding


def remove_padding(text, blocksize=64):

    counter = 0

    for c in text[::-1]:
        if c == '$':
            counter += 1
        else:
            break

    return text[:-counter]


def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(plain_text)


def decrypt(cipher_text, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(cipher_text).decode('UTF-8')


if __name__ == '__main__':

    key = 'secretaa'
    plain_text = 'This is the secret message we want to encrypt!'
    plain_text = add_padding(plain_text)
    cipher_text = encrypt(plain_text, key)

    decrypted_message = decrypt(cipher_text, key)
    decrypted_message = remove_padding(decrypted_message)
    print(decrypted_message)
