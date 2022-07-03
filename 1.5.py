a=int(input("podaj rok:"))

if a%4==0 and a%100!=0:
    print("Rok jest przestępny")
else:
    print("Jest to zwykły rok")