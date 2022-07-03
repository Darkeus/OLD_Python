a=int(input("Podaj liczbę: "))
b=1
c=1
if a>0:
    for i in range(0, a):
        c=c*b
        b=b+1
    print (c)
elif a==0:
    print(1)
else:
    print("Podano złą liczbę")


