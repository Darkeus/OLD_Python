
Suma=0
for i in range(0, 1000):
    x = 0
    liczba=int(i/2+1)
    for z in range(1, liczba):
        if i%z==0:
            x=x+z
    if i == x:
            Suma = Suma + i
print(Suma)

