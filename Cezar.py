a=(input('Podaj login: '))
b=(input('Podaj hasło: '))
haslo="okon"
login="MrK"
hash(login)
hash(haslo)
if a in [login] and b in [haslo]:
    print ("zalogowano")
    print (haslo)

else:
    print ("Błędne hasło lub login")
