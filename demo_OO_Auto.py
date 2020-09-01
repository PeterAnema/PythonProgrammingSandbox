class Auto:

    def __init__(self, merk, type, kleur, kmstand = 0):
        self.__merk = merk
        self.__type = type
        self.__kleur = kleur
        self.__kmstand = kmstand

    def __str__(self):
        return "Een %s %s kleur %s met %g km op de teller." % (self.__merk,
                                                               self.__type,
                                                               self.__kleur,
                                                               self.__kmstand)

    def __repr__(self):
        return "Auto(%s, %s, %s, %g)" % (self.__merk,
                                         self.__type,
                                         self.__kleur,
                                         self.__kmstand)

    def info(self):
        return "Een %s %s kleur %s met %g km op de teller." % (self.__merk,
                                                               self.__type,
                                                               self.__kleur,
                                                               self.__kmstand)

    def rijden(self, km):
        self.__kmstand += km

# ====================================================================

autos = []
autos.append( Auto('Opel', 'Astra', 'Zwart', 165000) )
autos.append( Auto('Renault', 'Megane', 'Bruin', 223089) )
autos.append( Auto('VW', 'Up!', 'Rood', 7465) )

for auto in autos:
    print(auto)

autos[0].rijden(102)
autos[1].rijden(357)
autos[2].rijden(1002)
autos[2].rijden(10)
autos[1].rijden(278)
autos[0].rijden(8)

for auto in autos:
    print(auto)

print(autos)

