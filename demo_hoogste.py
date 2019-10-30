def maximum(*getallen):
    hoogste = getallen[0]
    for getal in getallen[1:]:
        if getal > hoogste:
            hoogste = getal
    return hoogste

def minimum(*getallen):
    laagste = getallen[0]
    for getal in getallen[1:]:
        if getal < laagste:
            laagste = getal
    return laagste

def minimum_maximum(*getallen):
    laagste = getallen[0]
    hoogste = getallen[0]
    for getal in getallen[1:]:
        if getal > hoogste:
            hoogste = getal
        elif getal < laagste:
            laagste = getal
    return laagste, hoogste


# ------------------------------------

print( maximum(234, 567, 345, 687, 234, 46, 455) )
print( minimum(234, 567, 345, 687, 234, 46, 455) )

print( minimum_maximum(234, 567, 345, 687, 234, 46, 455) )

