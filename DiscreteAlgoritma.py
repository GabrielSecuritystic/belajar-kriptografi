# latihan memahami algoritma discrete kriptografi


"""
Rumus algoritma diskrit:

-.jika a adalah akar primitf dari bilangan prima p,maka untuk bilangan bulat b kita dapat menemukan pangkat i,rumus:
b = a^x(mod p) gambaran-> 0<=x<=(p-1)

keterangan
^ adalah simbol perpangkatan

Note:
pangkat x disebut logaritma diksrit dari b untuk basis a(mod p).
Didalam logaritma baisa bahwa dari perapngkatan y = g^x kita dapat menghitung nilai dari x sebagai logaritma y dengan basis g,yaitu x = g log y
"""
# membuat function untuk mendefinsikan algoritma diskrit

def algoritma_diskrit(a, b, m):

    c = 1

    # melakukan looping jika b^c mod m = a
    # artinya jika b akar dari c modulus m maka hasilnya adalah a
    c = c+1

    return c

# membuat function untuk melakukan eksponen


def modular_exponential(b, c, m):
    return pow(b, c) % m


# membuat script kompiler agar skrip diatas bisa dirunning
if __name__ == '__main__':
    print(modular_exponential(5, 948603, 9048610007))
    print(algoritma_diskrit(3668993056, 5, 9048610007))
