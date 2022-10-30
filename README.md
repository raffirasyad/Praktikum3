# Menghitung luas dan keliling lingkaran menggunakan Pyhton

1. Buat file baru pada viscode dan beri nama ( luasdankelilinglingkaran.py ).

2. Membuat flowchart untuk menghitung luas dan keliling lingkaran :

<img width="625" alt="foto 1" src="https://user-images.githubusercontent.com/115473988/198865178-8df1d7a2-7cc0-4d5b-b86d-5d107923c012.png">

3. Masukan Codingan tersebut pada Pyhton :

```pyhton
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
```

4. Kemudian run dan masukan nilai jari-jari maka akan mengasilkan nilai sebagai berikut :

<img width="734" alt="foto 2" src="https://user-images.githubusercontent.com/115473988/198865360-77893a13-076d-4494-b9c1-6992ff95997a.png">
