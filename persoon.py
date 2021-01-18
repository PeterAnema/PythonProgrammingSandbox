class Persoon:
    __slots__ = ('naam', 'woonplaats', 'leeftijd')

    def __init__(self, naam, woonplaats, leeftijd):
        self.naam = naam
        self.woonplaats = woonplaats
        self.leeftijd = leeftijd

    def vertel(self):
        return f'Ik ben {self.naam}. Ik woon in {self.woonplaats}. En ik ben {self.leeftijd}.'

    def verhuis(self, nieuwe_woonplaats):
        self.woonplaats = nieuwe_woonplaats

class str:

    def __init__(self, s):
        self.content = s

    def output(self):
        print(self.content)
        