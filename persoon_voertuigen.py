

class Persoon(object) :
    """Dit is het Persoon class"""

    def __init__(self, naam='onbekend'):
        self.naam = naam
        self.voertuigen = []

    def __repr__(self):
        return '%s(%s)' % (__class__, self.naam)

    def __str__(self):
        return self.naam + '\n' + self.geefLijstVanVoertuigen()

    def koopVoertuig(self, voertuig):
        self.voertuigen.append(voertuig)

    def verkoopVoertuig(self, voertuig):
        self.voertuigen.remove(voertuig)

    def geefLijstVanVoertuigen(self):
        return '\n'.join([str(voertuig) for voertuig in sorted(self.voertuigen)])

class Voertuig (object):
    """Dit is het Voertuig class"""

    def __init__(self, kenteken='onbekend', merk='onbekend', model='onbekend', aantalKilometers=0):
        self.kenteken = kenteken
        self.merk = merk
        self.model = model
        self.__aantalKilometers = aantalKilometers

    def __eq__(self, other):
        return self.__aantalKilometers == other.__aantalKilometers
    def __ne__(self, other):
        return self.__aantalKilometers != other.__aantalKilometers
    def __lt__(self, other):
        return self.__aantalKilometers < other.__aantalKilometers
    def __le__(self, other):
        return self.__aantalKilometers <= other.__aantalKilometers
    def __gt__(self, other):
        return self.__aantalKilometers > other.__aantalKilometers
    def __ge__(self, other):
        return self.__aantalKilometers >= other.__aantalKilometers

    def __repr__(self):
        return '%s(%s, %s, %s, %d)' % (__class__, self.kenteken, self.merk, self.model, self.__aantalKilometers)

    def __str__(self):
        return '%s: %s %s (%d km)' % (self.kenteken, self.merk, self.model, self.__aantalKilometers)

    def rijden(self,aantalKilometers):
        self.__aantalKilometers += aantalKilometers


class Vrachtwagen(Voertuig) :
    """Dit is het Vrachtwagen class"""

    def __init__(self, kenteken='onbekend', merk='onbekend', model='onbekend', aantalKilometers=0, laadVermogen=0):
        super().__init__(kenteken, merk, model, aantalKilometers)
        self.__laadVermogen = laadVermogen

    def __repr__(self):
        return '%s(%s, %s, %s, %d, %d)' % (__class__,
                                           self.kenteken,
                                           self.merk,
                                           self.model,
                                           self.__aantalKilometers,
                                           self.__laadvermogen)

    def __str__(self):
        return super().__str__() + ' met %d kg laadvermogen' % self.__laadVermogen

    
class Bus(Voertuig) :
    """Dit is het Bus class"""

    def __init__(self, kenteken='onbekend', merk='onbekend', model='onbekend', aantalKilometers=0, maximaalAantalPassagiers=0):
        super(Bus,self).__init__(kenteken, merk, model, aantalKilometers)
        self.__maximaalAantalPassagiers = maximaalAantalPassagiers
        self.__aantalPassagiers = 0

    def instappen(self, aantal) :
        self.__aantalPassagiers += min(aantal, self.__maximaalAantalPassagiers - self.__aantalPassagiers)

    def uitstappen(self,aantal) :
        self.__aantalPassagiers -= aantal

    def __repr__(self):
        return '%s(%s, %s, %s, %d, %d)' % (__class__,
                                           self.kenteken,
                                           self.merk,
                                           self.model,
                                           self.__aantalKilometers,
                                           self.__aantalPassagiers)

    def __str__(self):
        return super().__str__() + ' met %d passagiers' % self.__aantalPassagiers


# Client code ----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    persoon1 = Persoon('Peter')

    voertuig1 = Voertuig('99-EE-45', 'Volkswagen', 'Kever', aantalKilometers=56930)
    voertuig2 = Voertuig('22-EE-45', 'Volkswagen', 'Kever', aantalKilometers=76923)
    voertuig2.rijden(2210)
    voertuig2.rijden(1011)
    voertuig2.rijden(1312)
    voertuig2.rijden(110)

    persoon1.koopVoertuig(voertuig1)
    persoon1.koopVoertuig(voertuig2)

    persoon1.verkoopVoertuig(voertuig1)
    persoon1.koopVoertuig(Voertuig('STH-ER-99', 'Renault', 'Megane', aantalKilometers=26935))

    voertuig3 = Vrachtwagen('9-EE-405', 'Volvo', 'Vracht', laadVermogen=1200, aantalKilometers=246978)
    persoon1.koopVoertuig(voertuig3)

    voertuig4 = Bus('EE-45-34', 'Mercedes', 'Minibus', maximaalAantalPassagiers=20, aantalKilometers=103849)
    persoon1.koopVoertuig(voertuig4)

    voertuig4.instappen(4)
    voertuig4.instappen(6)
    voertuig4.uitstappen(2)
    voertuig4.instappen(5)

    print(persoon1)
