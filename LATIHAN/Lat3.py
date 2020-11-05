def faktorial(n):
    faktorial=1
    i=n
    while i>=1:
        faktorial*=i
        i-=1
    return(faktorial)

n=4
print('Contoh:')
print('~',n,'faktorial =',faktorial(n))
print('')

#soal no.3a C(5,3)
a=5
b=3
print('a. tentukan nilai dari C(',a,',',b,')')
kombinasi = faktorial(a)/(faktorial(b)*faktorial(a-b))
print('   ~Hasil dari kombinasi C(',a,',',b,') adalah',kombinasi)
print('')

#soal no.3b P(10, 7)
p=10
q=7
print('a. tentukan nilai dari P(',p,',',q,')')
permutasi = faktorial(p)/ faktorial(p-q)
print('   ~Hasil dari permutasi P(',p,',',q,') adalah',permutasi)
print('')
