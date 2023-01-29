import random
"""
Cara kerja Algoritma DiffieHellman
contoh:
1.Alice membangkitkan bilangan bulat acakx dan mengirim hasil perhitungan berikut kepada bob:
X = g^x mod n

2.Bob membangkitkan bilangan bulat acak y dan mengirim hasil perhitungan berikut kepada Alice:
Y = g^y mod n

3.Alice menghitung
K =Y^X mod n

4.Bob menghitung
K =X^Y mod n

keterangan
g adalah bilangan bulat yang memiliki akar primitif
n adalah bilangan prima
^ adalah simbol perpangkatan


langkah-langkah melakukan decrypt algoritma DiffieHellman:
1. melakukan perhitungan logaritma diskrit untuk menemukan X dari persamaan X = g^x mod n
2.jika nilai X sudah ditemukan,maka gunakan rumus K = Y^X mod n

keterangan
K artinya key
"""
# membuat function untuk generate private key


def generate_private_key(n, g):
    # membuat random number generator untuk aktor pertama x<n-1
    x = random.randint(1, n)
    # membuat random number generator untuk aktor kedua y<n-1
    y = random.randint(1, n)

    # menghitung g^x modulus n yang mana disini akan digunakan sebagai key1/k1
    k1 = pow(g, x, n)
    # menghitung g^x modulus n yang mana disini akan digunakan sebagai key2 atau k2
    k2 = pow(g, y, n)

    # mencetak hasil generate private key yang dimiliki aktor pertama dan kedua
    # dimana hasil private key dari dua aktor tersebut harus sama karena disini menggunakan algoritma DiffieHellman

    print("Aktor pertama memiliki private key %s" % (pow(k1, x, n)))
    print("Aktor kedua memiliki private key %s" % (pow(k2, x, n)))


# membuat script compile agar script tersebut bisa running
if __name__ == "__main__":
    # nilai dari variable n harus angka prima
    n = 37
    # nilai dari variable g  adalah angka primitif dari angka yang ditentukan angka prima tersebut
    g = 13

    # menggunakan algoritma DiffieHellman untuk generate private key
    generate_private_key(n, g)
