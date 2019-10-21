import re

def aantal_woorden(tekst):
    return len(verwijder_leestekens(tekst).split())

def verwijder_leestekens(tekst):
    return tekst.translate(str.maketrans('','','.,:;?!&()[]{}')).strip()

def aantal_letters(tekst):
    return len(verwijder_leestekens(tekst).replace(' ', ''))

def aantal_lettergrepen(woord):
    regex = re.compile(r'aai|ooi|qua|quo|aa|ai|au|ee|eë|ei|ey|ie|ij|oe|oo|ou|ui|uu|uy|a|e|i|o|u|y|ä|ë|ï|ö|ü', re.IGNORECASE)
    return len(regex.findall(woord))

def aantal_zinnen(tekst):
    regex = re.compile(r'\w{2}[\.!\?]', re.IGNORECASE)
    n = len(regex.findall(tekst))

    if tekst.strip() and not re.search(r'[\.!\?]\s*$', tekst, re.IGNORECASE):
        n += 1

    return n

def gemiddeld_aantal_woorden_per_zin(tekst):
    n = aantal_zinnen(tekst)
    return aantal_woorden(tekst) / n if n else None

def gemiddelde_woordlengte(tekst):
    n = aantal_woorden(tekst)
    return aantal_letters(tekst) / n if n else None

def gemiddeld_aantal_lettergrepen_per_woord(tekst):
    n = aantal_woorden(tekst)
    return aantal_lettergrepen(tekst) / n if n else None

def leesbaarheidsindex(tekst):
    n = gemiddeld_aantal_lettergrepen_per_woord(tekst)
    if not n: return None
    woordlengte = n * 100

    n = gemiddeld_aantal_woorden_per_zin(tekst)
    if not n: return None
    zinslengte = n

    return flesch_douma_formule(woordlengte, zinslengte)

def flesch_douma_formule(woordlengte, zinslengte):
    """ Flesch-Doumaformule NL: 206,84 – (0,77 x woordlengte) – (0,93 x zinslengte) """
    return 206.84 - (0.77 * woordlengte) - (0.93 * zinslengte)
