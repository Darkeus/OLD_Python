a=int(input("Podaj długość podstawy: "))
h=int(input("Podaj wysokość: "))
p=(a*h)/2
if p>0:
    print("Pole trójkąta wynosi:" + str(p))
else:
    print("Podano złe wymiary")