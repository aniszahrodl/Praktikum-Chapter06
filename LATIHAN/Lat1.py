def isPytagoras(a, b, c):
    p=a**2
    q=b**2
    r=c**2
    if r==(p+q):
        print('a =',a,', b =',b,', c =',c,' ->',True)
    else:
        print('a =',a,', b =',b,', c =',c,' ->',False)

isPytagoras(3, 4, 5)
isPytagoras(5, 9, 12)
isPytagoras(8, 6, 10)
isPytagoras(7, 8, 11)
