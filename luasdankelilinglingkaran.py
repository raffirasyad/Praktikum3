# import module math
import math

# Variable jarijari
jarijari = input('Masukan jari-jari lingkaran :')

"""

rumus luas & keliling lingkaran
_______________________________

luas = phi * r^2

keliling = 2 * phi * r
_______________________________

"""
# convert string to integer
jarijari = int(jarijari)

# hitung luas lingkaran
luas = math.pi * (jarijari * jarijari)

# hitung luas keliling 
keliling = 2 * math.pi * jarijari

# output luas & keliling lingkaran
# .2f => mengambil 2 angka setelah (,)
print("Berikut luas lingkaran = ", format(luas, '.2f') )
print("Berikut keliling lingkaran = ", format(keliling, '.2f'))
