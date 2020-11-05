from operation import *

#soal 5c. (10+12)/(7+12)/(12-34)
a=10
b=2
c=7
d=5
e=12
f=34


print('(',a, '+', b,')/(',c, '+', d,')/(',e, '-', f,') =',
      bagi(bagi(jumlah(a,b),jumlah(c, d)), kurang(e, f)))
