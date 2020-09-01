kluisjes = []

def selecteer_kluis(kluisnummer):
    for kluis in kluisjes:
        if kluis['kluisnr'] == kluisnummer:
            return kluis

def reserveer_kluis(kluisnummer, pincode):
    kluis = selecteer_kluis(kluisnummer)
    kluis['pincode'] = pincode
    kluis['beschikbaar'] = False

def geef_kluis_vrij(kluisnummer):
    kluis = selecteer_kluis(kluisnummer)
    kluis['pincode'] = None
    kluis['beschikbaar'] = True

def beschikbare_kluisnummers():
    return [kluis['kluisnr'] for kluis in kluisjes if kluis['beschikbaar']]

def gebruiker_welkom():
    print('Welkom bij de sportschool, Wesley Blijlevens!')
    print('Voordat je kan sporten, moet je eerst een kluis reserveren!')

def gebruiker_reserveer_kluisje():
    beschikbaar = beschikbare_kluisnummers()
    print('Deze kluisnummers zijn beschikbaar: ', *beschikbaar)
    while True:
        input_kluisnummer = int(input(f'Tik je gewenste kluisnummer in: '))
        if input_kluisnummer in beschikbaar:
            input_pincode = input('Geef hier je pincode voor de kluis! Let op pincode bestaat uit 4 cijfers!: ')
            reserveer_kluis(input_kluisnummer, input_pincode)
            print(f"De volgende kluisnummer {input_kluisnummer} is voor je gereserveerd. Sport ze!")
            break
        else:
            print('Kies svp alleen een van de beschikbare kluisnummers!')

def gebruiker_geef_kluisje_vrij():
    inputKluisnr = int(input('Wat is de kluisnummer? '))
    kluis = selecteer_kluis(inputKluisnr)
    if kluis:
        inputPincode = input('Wat is de pincode? ')
        if inputPincode == kluis['pincode']:
            geef_kluis_vrij(inputKluisnr)
            print(f'Kluisnummer {inputKluisnr} is nu geopend!')
            input('Klik maar op enter! Tot de volgende keer! :-)')
        else:
            print(f'De opgegeven pincode {inputPincode} is onjuist')
    else:
        print(f'Je opgegeven kluisnummer {inputKluisnr} bestaat niet of is reeds beschikbaar')

def gebruiker_kies_actie():
    input_keuze = input("Wil je keuze 1 (een kluis reserveren) of keuze 2 (een kluis vrijgeven)?: ")

    if input_keuze == '1':  # een kluis reserveren
        gebruiker_reserveer_kluisje()

    elif input_keuze == '2':  # een kluis vrijgeven
        gebruiker_geef_kluisje_vrij()

    elif input_keuze == 'x':
        return 'x'

    else:
        print(f'Je kunt alleen keuze 1 of 2 kiezen! Je toetste {input_keuze}')

# ----------------------------------------------------------------------

"""Er zijn 7 kluisjes in de sportschool (2 reeds bestaan)"""

aantal_kluisjes = 7
kluisjes += [{'kluisnr': i + 1,
              'pincode': None,
              'beschikbaar': True} for i in range(aantal_kluisjes)]

reserveer_kluis(1, '6432')
reserveer_kluis(2, '9269')

# print(kluisjes)

gebruiker_welkom()
while True:
    actie = gebruiker_kies_actie()
    if actie == 'x':
        break

# print(kluisjes)
