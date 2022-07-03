tablica = []
tablica.append(2)
tablica.append(44)
tablica.append(21)
tablica.append(231)
tablica.append(222)
z=5
while z >= 2:
    k=0
    while k<4:
        if tablica[k] > tablica[k+1]:
            x=tablica[k]
            tablica[k]=tablica[k+1]
            tablica[k+1]= x
        k += 1
    z -= 1
print(tablica[0])
print(tablica[1])
print(tablica[2])
print(tablica[3])
print(tablica[4])