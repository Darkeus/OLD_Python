pierwsze=[]

for a in range(0, 100):
    c=[]
    for i in range(1,a+1):
        if a%i==0:
            c.append(i)
    if len(c)==2:
        pierwsze.append(a)
print(pierwsze)
