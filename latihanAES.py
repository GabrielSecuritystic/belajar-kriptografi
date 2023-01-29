# latihan implementasi Algoritma Kriptografi AES

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

"""
Proses Cara Enkripsi dan Dekripsi Kriptografi AES

Proses dekripsi adalah kebalikan dari dekripsi. Karena terjadi beberapa tahap dalam proses enkripsi, maka diperlukan subkey-subkey yang akan dipakai pada tiap tahap. Pengembangan jumlah kunci yang akan dipakai diperlukan karena kebutuhan subkey-subkey yang akan dipakai dapat mencapai ribuan bit, sedangkan kunci yang disediakan secara default hanya 128-256 bit. Jumlah total kunci yang diperlukan sebagai subkey adalah sebanyak Nb(Nr+1), dimana Nb adalah besarnya blok data dalam satuan word. Sedangkan Nr adalah jumlah tahapan yang harus dilalui dalam satuan word. Sebagai contoh, apabila digunakan 128 bit (4 word) blok data dan 128 bit (4 word) kunci maka akan dilakukan 10 kali proses. Dengan demikian dari rumus didapatkan 4(10+1)=44 word=1408 bit kunci. Untuk melakukan pengembangan jumlah kunci yang akan dipakai dari kunci utama maka dilakukan key schedule.
EKSPANSI KUNCI

Algoritma AES mengambil kunci cipher, K, dan melakukan rutin ekspansi kunci (key expansion) untuk membentuk key schedule. Ekspansi kunci yang diperlukan AES Nb(Nr+1) word, sehingga bisa digunakan AES 128 bit maka, 4(10+1) = 40 word = 44 x 32 bit = 1408 bit sub key. Ekspansi dari 128 menjadi 1408 bit subkey. Proses ini disebut dengan key schedule. Subkey ini diperlukan karena setiap round merupakan suatu nilai inisial dari Nb word untuk Nr = 0 dan 2 untuk Nr = 1,3 untuk Nr = 2,….., yang berisi array linier empat byte word (w), 0=1 Nb(Nr + 1).

Contoh dari ekspansi kunci seperti di bawah ini :

RotWord() engambil input empat-byte word [ dan membentuk cyclic permutasi seperti [a1,a2,a3,a0]’
Sub word() mengambil input empat-byte word dan menggunakan S-Box sehingga didapat empat byte output dari prosedur.
Rcon() menghasilkan round yang tetap dari word array dan berisi nilai yang diberikan oleh [[xid1, {00}, {00}, {00}, {00}] dengan xid1 dari I ke 1.
Rcon[i] = [[xid1, {00}, {00}, {00}, {00}]
Rcon [1] = [x0, {00}, {00}, {00}, {00}] = [{01}, {00}, {00}, {00}] = 01000000
Rcon [2] = [x1, {00}, {00}, {00}, {00}] = 02000000
Rcon [3] = [x2, {00}, {00}, {00}, {00}] = 04000000
Rcon [4] = [x3, {00}, {00}, {00}, {00}] = 08000000
Rcon [5] = [x4, {00}, {00}, {00}, {00}] = 10000000
Rcon [6] = [x5, {00}, {00}, {00}, {00}] = 20000000
Rcon [7] = [x6, {00}, {00}. {00}, {00}] = 40000000
Rcon [8] = [x7, {00}, {00}, {00}, {00}] = 80000000
Rcon [9] = [x8, {00}, {00}, {00}, {00}] = [x7] · x, {00}, {00}, {00}] = 1b000000
        x7 · x = xtime(x7) = xtime(80) = {leftshift(80)} · “ {1b} = 1b
Rcon [10] = [x9, {00}, {00}, {00}] = [x8 · x, {00}, {00}, {00}] = 36000000
Rcon [11] = [x10, {00}, {00}, {00}] = [x9 · x, {00}, {00}, {00}] = 6c000000
Rcon [12] = [x11, {00}, {00}, {00}] = [x10 · x, {00}, {00}, {00}] = d8000000
Rcon [13] = [x12, {00}, {00}, {00}] = [x11 · x, {00}, {00}, {00}] = ab000000
       X11 · x = xtime(x11) = xtime (d8)= {leftshift (d8)} · “ {1b} = ab



Rcon[ i ] adalah suatu komponen dari round tetap word array dalam perhitungan ekspansi key routine


PROSES ENKRIPSI
Enkripsi dengan menggunakan AES
Secara umum enkripsi dengan algoritma AES sebagai berikut :
Pertama kita melakukan XOR plainteks/ state dengan roundkey.
Setelah selesai melakukan XOR plainteks dengan roundkey, kita lakukan substitusi dengan s-Box
Setelah itu hasil dari substitusi dengan S-Box Selesai kita lakukan shift row
Setelah hasil shift row di dapat, maka langkah selanjutnya yaitu melakukan Mix Column dengan cara megalikan matrik
Setelah perhitungan Mix Column selesai maka kita melakukan addround key. Yaitu melakukan XOR state dengan roundkey. Lakukan samapai iterasi 10, namun pada saat iterasi ke 10, setelah melakukan step shift row tidak melakukan Mix Colum. Namun langsung melakukan XOR hasil state saat shift row dengan round key.
"""


class AESCipher:

    # membuat constructor
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    # membuat function untuk menambahkan sebuah data/generate random data
    def add_padding(self, plaintext):
        bytes_to_pad = self.block_size - len(plaintext) % self.block_size

        # membuat CMS atau PKCS (Cryptographic Messsage Syntax)
        ascii_string = chr(bytes_to_pad)
        padding_string = ascii_string * bytes_to_pad
        return plaintext + padding_string

    # membuat function untuk menghapus semua generate data
    def remove_padding(self, txt):
        last_character = txt[len(txt)-1:]
        return txt[:-ord(last_character)]

    # membuat function untuk melakukan aksi encrypt data
    def encrypt(self, plaintext):
        plaintext = self.add_padding(plaintext)
        # membuat sebuah IV(Initialization Vector - Seed)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plaintext.encode())
        return b64encode(iv+encrypted_text).decode('utf-8')

    # membuat function untuk melakukan aksi decrypt data
    def decrypt(self, encrypted):
        encrypted = b64decode(encrypted)
        iv = encrypted[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(
            encrypted[self.block_size:]).decode('utf-8')
        return self.remove_padding(plaintext)


# membuat script untuk compile agar program bisa di running
if __name__ == '__main__':
    aes = AESCipher('Indonesia Raya')
    # plain = str(aes)
    message = 'Contoh Implementasi algoritma kritografi AES'
    print(aes.__dict__)

    encrypted = aes.encrypt(message)
    print(encrypted)
    print(aes.decrypt(encrypted))
