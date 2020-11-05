def Sum(*myData):
    Sum = 0
    i = 0
    for data in myData:
        Sum += data
        i += 1
    print('Jumlah seluruh bilangan:',Sum)

def Average(*myData):
    Sum = 0
    i = 0
    for data in myData:
        Sum += data
        i += 1
    Average= Sum/i
    print('Rata-rata:',Average)

def Maks(*myData):
    Maks = -999999999
    for data in myData:
        if data > Maks:
            Maks = data
    print('Nilai maksimum:',Maks)

def Min(*myData):
    Min = 999999999
    for data in myData:
        if data < Min:
            Min = data
    print('Nilai Minimum:',Min)





    

