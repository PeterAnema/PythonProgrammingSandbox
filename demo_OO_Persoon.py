
class Persoon(object):

    def __init__(self, naam, woonplaats):
        self.naam = naam
        self.woonplaats = woonplaats

    def vertel(self):
        print('Ik ben %s en ik woon in %s' % (self.naam, self.woonplaats))

    def verhuis(self, nieuwe_woonplaats):
        self.woonplaats = nieuwe_woonplaats


# ==============================================================================

if __name__ == '__main__':

    p1 = Persoon('Peter', 'Lhee')
    p1.vertel()

    p2 = Persoon('Marco', 'Den Haag')
    p2.vertel()

    p1.verhuis('Groningen')
    p1.vertel()
