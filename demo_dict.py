'''A dictionary of area codes'''

d = {'rijswijk': ('070','ZH'),
     'leiden': ('071','ZH')}

d['amsterdam'] = '020', 'NH'
d['utrecht'] = '030', 'UT'
d['rotterdam'] = '010', 'ZH'
d['den haag'] = '070', 'ZH'
d['eindhoven'] = '040', 'NB'
d['groningen'] = '050', 'GR'
d['zwolle'] = '053', 'OV'
d['delft'] = '015', 'ZH'
d['zwolle'] = '057', 'OV'

plaats = input('Geef een plaats: ').lower()
print("Netnummer van %s is %s" % (plaats.title(), d.get(plaats)[0]))

netnummer = input('Geef een netnummer: ')
for plaats, t in d.items():
    if t[0] == netnummer:
        print("Netnummer %s hoort bij %s" % (netnummer, plaats))
