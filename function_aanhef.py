
def aanhef(voornaam, achternaam, mv = None):

    naam = f'{voornaam} {achternaam}'

    if mv == 'v':
        return 'Geachte mevrouw ' + naam
    elif mv == 'm':
        return 'Geachte heer ' + naam
    else:
        return 'Beste ' + naam


# -------------------------------------

if __name__ == '__main__':

    print(aanhef('Peter', 'Anema', 'm'))
    print(aanhef('Robin', 'Meester', 'v'))
    print(aanhef('Mael', 'van Dijk', 'x'))