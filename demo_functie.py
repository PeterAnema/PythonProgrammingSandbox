

def bepaal_grootste(*getallen):
    grootste = 0
    for getal in getallen:
        if getal > grootste:
            grootste = getal
    return grootste


print(bepaal_grootste(1,4,2,5,99,4,7,2,3,23))
