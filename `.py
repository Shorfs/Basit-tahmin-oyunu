#Basit Tahmin Oyunu.

import random

print('Tahmin oyununa hosgeldiniz')

t_sayisi = random.randint(1, 70)
d_hakki = 7

while True:
    try:
        tahmin = int(input('(1 - 70) Sayinizi giriniz: '))
        if tahmin == t_sayisi:
            print('Tebrikler sayiyi dogru bildiniz. Dogru sayimiz {}'.format(t_sayisi))
            break
        elif tahmin < t_sayisi:
            print('Sayi kucuk')
        else:
            print('Sayi buyuk')

        d_hakki -= 1

        if d_hakki == 0:
            print('Deneme sansiniz kalmadi')
            break
    except ValueError:
        print('Sayi girdiginize emin olun')