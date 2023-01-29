import random

"""
Rumus Algoritma kriptografi OTP

-.encrypt OTP:
c = (p+k) mod 26

keterangan:
c adalah ciphertext
p adalah plaintext
k adalah key
mod adalah modulus atau sisa hasil bagi

-.decrypt OTP:
p = (c-k) mod 26

Note:
untuk kode OTP yang dihasilkan itu secara acak dan secara berkala,maka setiap kali refresh atau memuat ulang akan terus menerus diganti

"""
#kode acak yang akan digunakan untuk membuat OTP
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main():
    """Demo usage of functions."""
    #variable vectory berisi plaintext yang akan dibuat otp,encrypt dan decrypt
    vector = "goodmorning"
    encrypted = encrypt(vector)
    #membuat decrypt dimana index ke 0 akan diganti menjadi index ke.1
    decrypted = decrypt(encrypted[0], encrypted[1])

    #mencetak sebuah plaintext
    print("Test Vector: " + vector)
    #mencetak hasilOTP yang berhasil dibuat
    print("OTP: " + encrypted[0])
    #mencetak hasil encrypt data yang berhasil dibuat dan encrypt data dimulai dari index ke.1
    print("Encrypted: " + encrypted[1])
    #mencetak hasil decrypt
    print("Decrypted: " + decrypted)


def encrypt(plaintext):
    """Encrypt plaintext value.
    Keyword arguments:
    plaintext -- the plaintext value to encrypt.
    """
    otp = "".join(random.sample(charset, len(charset)))
    result = ""

    for c in plaintext.upper():
        if c not in otp:
            continue
        else:
            result += otp[charset.find(c)]

    return otp, result


def decrypt(otp, secret):
    """Decrypt secret value.
    Keyword arguments:
    otp -- the one-time pad used when the secret value was encrypted.
    secret -- the value to be decrypted.
    """
    result = ""

    for c in secret.upper():
        if c not in otp:
            continue
        else:
            result += charset[otp.find(c)]

    return result


if __name__ == "__main__":
    main()
