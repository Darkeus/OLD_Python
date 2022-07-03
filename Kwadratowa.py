from math import sqrt
a=int(input('Podaj a: '))
b=int(input('Podaj b: '))
c=int(input('Podaj c: '))
delta= b * b + 4 * a * c
if delta >0:
    print("Istnieją dwa miejsca zerowe:")
    x1= (-b-sqrt(delta))/2*a
    x2= (-b+sqrt(delta))/2*a
    print (x1,x2)
elif delta == 0:
    print("Istnieje jedno miejsce zerowe: ")
    x0= (-b)/2*a
    print (x0)
else:
    print('Funkcja nie ma miejsc zerowych')