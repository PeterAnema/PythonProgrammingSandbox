import re

class Leesbaarheidsindex:

    def __init__(self, tekst):
        self.set_tekst(tekst)

    def set_tekst(self, tekst):
        self.__tekst = tekst
        self.__aantal_zinnen = None
        self.__aantal_woorden = None
        self.__aantal_lettergrepen = None
        self.__aantal_letters = None
        self.__leesbaarheidsindex = None

    def get_aantal_zinnen(self):
        if self.__aantal_zinnen is None:
            self.__aantal_zinnen = Leesbaarheidsindex.bepaal_aantal_zinnen(self.__tekst)
        return self.__aantal_zinnen

    def get_aantal_woorden(self):
        if self.__aantal_woorden is None:
            self.__aantal_woorden = Leesbaarheidsindex.bepaal_aantal_woorden(self.__tekst)
        return self.__aantal_woorden

    def get_aantal_lettergrepen(self):
        if self.__aantal_lettergrepen is None:
            self.__aantal_lettergrepen = Leesbaarheidsindex.bepaal_aantal_lettergrepen(self.__tekst)
        return self.__aantal_lettergrepen

    def get_aantal_letters(self):
        if self.__aantal_letters is None:
            self.__aantal_letters = Leesbaarheidsindex.bepaal_aantal_letters(self.__tekst)
        return self.__aantal_letters

    def get_gemiddeld_aantal_woorden_per_zin(self):
        n_zinnen = self.get_aantal_zinnen()
        n_woorden = self.get_aantal_woorden()
        return n_woorden / n_zinnen if n_zinnen else None

    def get_gemiddelde_woordlengte(self):
        n_woorden = self.get_aantal_woorden()
        n_letters = self.get_aantal_letters()
        return n_letters / n_woorden if n_woorden else None

    def get_gemiddeld_aantal_lettergrepen_per_woord(self):
        n_woorden = self.get_aantal_woorden()
        n_lettergrepen = self.get_aantal_lettergrepen()
        return n_lettergrepen / n_woorden if n_woorden else None

    def get_leesbaarheidsindex(self):
        if self.__leesbaarheidsindex is None:

            n_lettergrepen_per_woord = self.get_gemiddeld_aantal_lettergrepen_per_woord()
            if not n_lettergrepen_per_woord: return None
            woordlengte = n_lettergrepen_per_woord * 100

            n_aantal_woorden_per_zin = self.get_gemiddeld_aantal_woorden_per_zin()
            if not n_aantal_woorden_per_zin: return None
            zinslengte = n_aantal_woorden_per_zin

            self.__leesbaarheidsindex = Leesbaarheidsindex.flesch_douma_formule(woordlengte, zinslengte)

        return self.__leesbaarheidsindex


    # static methods

    @staticmethod
    def __verwijder_leestekens(tekst):
        return tekst.translate(str.maketrans('', '', '.,:;?!&()[]{}')).strip()

    @staticmethod
    def bepaal_aantal_woorden(tekst):
        return len(Leesbaarheidsindex.__verwijder_leestekens(tekst).split())

    @staticmethod
    def bepaal_aantal_letters(tekst):
        return len(Leesbaarheidsindex.__verwijder_leestekens(tekst).replace(' ', ''))

    @staticmethod
    def bepaal_aantal_lettergrepen(woord):
        regex = re.compile(r'aai|ooi|qua|quo|aa|ai|au|ee|eë|ei|ey|ie|ij|oe|oo|ou|ui|uu|uy|a|e|i|o|u|y|ä|ë|ï|ö|ü',
                           re.IGNORECASE)
        return len(regex.findall(woord))

    @staticmethod
    def bepaal_aantal_zinnen(tekst):
        regex = re.compile(r'\w{2}[\.!\?]', re.IGNORECASE)
        n = len(regex.findall(tekst))

        if tekst.strip() and not re.search(r'[\.!\?]\s*$', tekst, re.IGNORECASE):
            n += 1

        return n

    @staticmethod
    def bepaal_gemiddeld_aantal_woorden_per_zin(tekst):
        n = Leesbaarheidsindex.aantal_zinnen(tekst)
        return Leesbaarheidsindex.aantal_woorden(tekst) / n if n else None

    @staticmethod
    def bepaal_gemiddelde_woordlengte(tekst):
        n = Leesbaarheidsindex.aantal_woorden(tekst)
        return Leesbaarheidsindex.aantal_letters(tekst) / n if n else None

    @staticmethod
    def bepaal_gemiddeld_aantal_lettergrepen_per_woord(tekst):
        n = Leesbaarheidsindex.aantal_woorden(tekst)
        return Leesbaarheidsindex.aantal_lettergrepen(tekst) / n if n else None

    @staticmethod
    def bepaal_leesbaarheidsindex(tekst):
        n = Leesbaarheidsindex.gemiddeld_aantal_lettergrepen_per_woord(tekst)
        if not n: return None
        woordlengte = n * 100

        n = Leesbaarheidsindex.gemiddeld_aantal_woorden_per_zin(tekst)
        if not n: return None
        zinslengte = n

        return Leesbaarheidsindex.flesch_douma_formule(woordlengte, zinslengte)

    @staticmethod
    def flesch_douma_formule(woordlengte, zinslengte):
        """ Flesch-Doumaformule NL: 206,84 – (0,77 x woordlengte) – (0,93 x zinslengte) """
        return 206.84 - (0.77 * woordlengte) - (0.93 * zinslengte)
