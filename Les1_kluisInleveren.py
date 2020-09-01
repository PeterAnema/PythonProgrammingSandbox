kluisjes = [
    {'kluisnr': 1, 'pincode': '6432', 'beschikbaar': False},
    {'kluisnr': 2, 'pincode': '9269', 'beschikbaar': False},
]

aantal_kluisjes = 7
kluisjes = [{'kluisnr': i + 1, 'pincode': None, 'beschikbaar': True} for i in range(aantal_kluisjes)]


def selecteerKluis(kluisnr):
    for kluis in kluisjes:
        if kluis['kluisnr'] == kluisnr:
            return kluis


def reserveerKluis(kluisnr, pincode):

            kluis['pin'] = pincode
            kluis['beschikbaar'] = False


if kluisnr in lijstVanAlleKluisjes.keys():
    lijstVanAlleKluisjes[kluisnr] = [kluisnr, pincode, False]
    print(f"De volgende kluisnummer {kluisnr} is voor je gereserveerd. Sport ze!")

"""Er zijn 7 kluisjes in de sportschool (2 reeds bestaan)"""
for index in range(5):
    kluisnummer = index
    pincode = ''
    isBeschikbaar = True
    lijstVanAlleKluisjes[kluisnummer + 3] = [kluisnummer + 3, pincode, isBeschikbaar]
    index + 1
print(lijstVanAlleKluisjes.values())

lijstBeschikbareKluis = []


def vindBeschikbareKluis():
    for kluisnr in lijstVanAlleKluisjes.keys():  # reaching the keys of dict
        for value in lijstVanAlleKluisjes[kluisnr]:  # reaching every element in tuples
            if value == True:  # if match found..
                lijstBeschikbareKluis.append(lijstVanAlleKluisjes[kluisnr])


def kiesGewensteKluis():
    lijstBeschikbareKluis.pop(0)
    beschikbareKluisNummer = [kluisnr[0] for kluisnr in lijstBeschikbareKluis]
    print('Welkom bij de sportschool, Wesley Blijlevens!')
    print('Voordat je kan sporten, moet je eerst een kluis reserveren!')
    print('Deze kluisnummers zijn beschikbaar: ', beschikbareKluisNummer)
    inputKluis = int(input(f'Tik je gewenste kluisnummer in:'))
    if inputKluis in beschikbareKluisNummer:
        inputPincode = input('Geef hier je pincode voor de kluis! Let op pincode bestaat uit 4 cijfers!: ')
        print(inputPincode)
        return inputKluis, inputPincode
    else:
        print('Kies svp alleen 1 van de beschikbare kluisnummer!')


def reserveerKluis(kluisnr, pincode):
    if kluisnr in lijstVanAlleKluisjes.keys():
        lijstVanAlleKluisjes[kluisnr] = [kluisnr, pincode, False]
        print(f"De volgende kluisnummer {kluisnr} is voor je gereserveerd. Sport ze!")


def vindDeJuisteKluis():
    inputKluis = int(input('Wat is de kluisnummer?'))
    if inputKluis in lijstVanAlleKluisjes.keys() and lijstVanAlleKluisjes[inputKluis][2] == False:
        inputPincode = input('Wat is de pincode?')
        juistePincode = lijstVanAlleKluisjes[inputKluis][1]
        if inputPincode == juistePincode:
            lijstVanAlleKluisjes[inputKluis] = [inputKluis, '', True]
            print(f'Kluisnummer {inputKluis} is nu geopend!')
            input('Klik maar op enter!Tot de volgende keer!:-)')
        else:
            print(f'Je opgegeven pincode {inputPincode} is onjuist')
    else:
        print(f'Je opgegeven kluisnummer {inputKluis} bestaat niet of is reeds beschikbaar')


keuzeWatGebruikerWilDoen = input("Wil je keuze 1 (een kluis reserveren) of keuze 2 (een kluis vrijgeven)?:")
if (int(keuzeWatGebruikerWilDoen) == 1):  # een kluis reserveren
    vindBeschikbareKluis()
    inputGebruiker = kiesGewensteKluis()
    if type(inputGebruiker) == tuple:
        reserveerKluis(inputGebruiker[0], inputGebruiker[1])
elif (int(keuzeWatGebruikerWilDoen) == 2):  # een kluis vrijgeven
    vindDeJuisteKluis()
else:
    print(f'Je kunt alleen keuze 1 of 2 kiezen! Je toetste {keuzeWatGebruikerWilDoen}')

print('Als check de lijst van alle kluisjes: ', lijstVanAlleKluisjes)
