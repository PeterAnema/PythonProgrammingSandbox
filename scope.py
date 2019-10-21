naam = "Peter"

def zeg_iets() :
    global naam
    naam = "Dries"
    tekst = "Hello " + naam
    return tekst    

print(naam)
print(zeg_iets())
print(naam)
