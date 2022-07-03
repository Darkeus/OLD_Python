tablica = []
tablica.append(2)
tablica.append(2)
tablica.append(5)

z=len(tablica)
while z >= 2:
    k=0
    while k<len(tablica)-1:
        if tablica[k] > tablica[k+1]:
            x=tablica[k]
            tablica[k]=tablica[k+1]
            tablica[k+1]= x
        k += 1
    z -= 1
c=0
while c != len(tablica):
    print (tablica[c])
    c += 1
