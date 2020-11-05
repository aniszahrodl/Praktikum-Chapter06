def starFormation1(n):
    kolom = 0
    baris = n

    i = 0
    while (i < baris) :
       j = 0
       while (j <= kolom) :
           print('* ', end='')
           j += 1
       print(' ')
       i += 1
       kolom += 1

def starFormation2(n):
    kolom = n-1
    baris = n

    i = 0
    while (i < baris) :
       j = 0
       while (j <= kolom) :
           print('* ', end='')
           j += 1
       print(' ')
       i += 1
       kolom -= 1

def starFormation3(n):
    kolom = 0
    baris = n
    tengah = (n+1)/2

    i = 0
    while (i < baris) :
       j = 0
       while (j <= kolom) :
           print('* ', end='')
           j += 1
       print(' ')
       i += 1
       kolom += 1

       if(kolom==tengah):
           kolom==tengah
           baris==tengah
           i = 0
           while(i <= n):
               j = 1
               while(j <= kolom):
                   print('* ', end='')
                   j += 1
               print(' ')
               i += 1
               kolom -= 1

print('formasi 1:')              
starFormation1(4)
print('')
print('formasi 2:')
starFormation2(4)
print('')
print('formasi 3:')
starFormation3(7)
