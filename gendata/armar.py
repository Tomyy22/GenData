import os
import random

with open('data/apes1') as fa:
    apellidos = [line.rstrip() for line in fa]

with open('data/noms') as fa:
    nombres = [line.rstrip() for line in fa]

anios=[1998,1999,2000,2001,2002,2003]
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
dias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

for i in range(10000):
    n = random.choice(nombres)
    a = random.choice(apellidos).title()
    d = 35000000 + i
    dia = '{num:02d}'.format(num=random.choice(dias))
    mes = '{num:02d}'.format(num=random.choice(meses))
    fn = f"{dia}/{mes}/{random.choice(anios)}"
    print(f"{n},{a},{d},{fn}")
