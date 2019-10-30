'''To read a STA file with banking mutations
SWIFT MT940
'''

from collections import OrderedDict
import re
import csv
from datetime import date
from decimal import Decimal
import locale

# Set to users preferred locale:
locale.setlocale(locale.LC_ALL, '')
# Or a specific locale:
# locale.setlocale(locale.LC_NUMERIC, "en_DK.UTF-8")


# filename = '/Users/peter/!! Privé/!! Financiën/Bankmutaties/MT940180428220241.STA' # 2018
# filename = '/Users/peter/!! Privé/!! Financiën/Bankmutaties/MT940180428220225.STA' # Circum 2018
# filename = '/Users/peter/!! Privé/!! Financiën/Bankmutaties/MT940191021154842.STA' # Circum 2019
# filename = '/Users/peter/!! Privé/!! Financiën/Bankmutaties/MT940191021154904.STA' # 2019
# filename = '/Users/peter/!! Privé/!! Financiën/2019/Bankmutaties/ABN Amro/MT940191025135257.STA'
filename = '/Users/peter/!! Privé/!! Financiën/2019/Bankmutaties/ABN Amro/MT940191025135450.STA'

messages = []
message = {}
current_beginsaldo = 0

def convert_amount_from_string(amount_str: str) -> Decimal:
    return Decimal(amount_str.replace(',', '.'))

def convert_amount_to_string(amount: Decimal) -> str:
    return ('%.2f' % amount).replace('.', ',')

def convert_date_from_string(date_str: str) -> date:
    return date(int(date_str[0:2]) + 2000,
                int(date_str[2:4]),
                int(date_str[4:6]))

def convert_date_to_string(date: date) -> str:
    return date.strftime('%Y%m%d')

def handle_20(content, message):
    message.update({'bank': content})


def handle_25(content, message):
    message.update({'rekeningnummer': content})


def handle_28(content, message):
    message.update({'statementnummer': content})


def handle_60F(content, message):
    global current_beginsaldo

    credit_debet = content[:1]
    datum = convert_date_from_string(content[1:7])
    munt = content[7:10]
    saldo = convert_amount_from_string(content[10:])

    if credit_debet == 'D':
        saldo = -saldo

    current_beginsaldo = saldo

    message.update({'begin_credit_debet': credit_debet,
                    'begindatum': datum,
                    'begin_munt': munt,
                    'beginsaldo': saldo})


def handle_61(content, message):
    global current_beginsaldo
    valuta_datum = convert_date_from_string(content[:6])
    boek_datum = convert_date_from_string(content[:2] + content[6:10])
    credit_debet = content[10:11]
    bedrag = convert_amount_from_string(content[11:11 + content[11:].index('N')])

    if credit_debet == 'D':
        bedrag = -bedrag

    current_eindsaldo = current_beginsaldo + bedrag

    mutations = message.get('mutations')
    if mutations is None:
        mutations = []

    mutations.append({'valuta-datum': valuta_datum,
                      'boek-datum': boek_datum,
                      'transactie_credit_debet': credit_debet,
                      'beginsaldo': current_beginsaldo,
                      'bedrag': bedrag,
                      'eindsaldo': current_eindsaldo})

    message.update({'mutations': mutations})

    current_beginsaldo = current_eindsaldo


def handle_86a(content, message):
    description = content.replace('\n', '')

    components = [
        'TRTP',
        'CSID',
        'NAME',
        'MARF',
        'REMI',
        'IBAN',
        'BIC',
        'EREF'
    ]

    decoded = {}
    for component in components:
        regex = re.compile(r'\/' + component + r'\/([^\/]+?)(\/|$)')
        groups = regex.search(description)
        if groups:
            decoded[component] = groups[1]

    decoded['omschrijving'] = '\n'.join([f'{k}: {v}' for k, v in decoded.items()])
    decoded['description'] = description

    decoded['naam'] = decoded.get('NAME')
    decoded['tegenrekening'] = decoded.get('IBAN')

    mutations = message.get('mutations')
    if mutations:
        mutations[-1].update(decoded)


def handle_86b(content, message):

    components = [
        'SEPA',
        # 'BEA',
        'IBAN:',
        'BIC:',
        'NAAM:',
        'MACHTIGING:',
        'OMSCHRIJVING:',
        'KENMERK:',
        'INCASSANT:',
        'VOOR:',
    ]

    lines = content.split('\n')
    description = '\n'.join(line[0:33] + '\n' + line[33:] for line in lines)
    lines = description.split('\n')

    concatenated_lines = []
    for line in lines:
        if line:
            line_starts_with_a_component = False
            for component in components:
                if line.startswith(component):
                    line_starts_with_a_component = True
                    break
            if line_starts_with_a_component:
                concatenated_lines.append(line)
            else:
                if concatenated_lines:
                    concatenated_lines[-1] += line
                else:
                    concatenated_lines.append(line)

    description = '\n'.join(concatenated_lines)

    decoded = {}
    for component in components:
        regex = re.compile(r'\b' + component + r'\s*(.+?)$', re.MULTILINE)
        groups = regex.search(description)
        if groups:
            decoded[component.rstrip(':')] = groups[1]

    decoded['omschrijving'] = '\n'.join(['%s: %s' % (k, v) for k, v in decoded.items()])

    if not decoded['omschrijving']:
        decoded['omschrijving'] = '\n'.join(lines)

    decoded['description'] = description

    decoded['naam'] = decoded.get('NAAM', '')
    decoded['tegenrekening'] = decoded.get('IBAN', '')

    mutations = message.get('mutations')
    if mutations:
        mutations[-1].update(decoded)


def handle_86(content, message):

    if content.startswith('/'):
        handle_86a(content, message)
    else:
        handle_86b(content, message)



def handle_62F(content, message):
    credit_debet = content[:1]
    datum = convert_date_from_string(content[1:7])
    munt = content[7:10]
    saldo = convert_amount_from_string(content[10:])

    if credit_debet == 'D':
        saldo = -saldo

    message.update({'eind_credit_debet': credit_debet,
                    'einddatum': datum,
                    'eind_munt': munt,
                    'eindsaldo': saldo})


handlers = {
    '20': handle_20,  # Transaction Reference Number (TRN)
    '25': handle_25,  # Account identification
    '28': handle_28,  # Statement number
    '60F': handle_60F,  # Opening balance
    '61': handle_61,  # Statement line
    '86': handle_86,  # Description
    '62F': handle_62F,  # Closing balance
}


def proces_line(line, message):
    if line.startswith(':'):
        segments = line.split(':')
        tag = segments[1]
        handler = handlers[tag]
        handler(':'.join(segments[2:]), message)


try:
    with open(filename, 'r') as f:

        print(f'processing file {filename}')

        codeline = ''
        current_beginsaldo = 0

        linenr = 0
        while True:
            try:
                linenr += 1
                line = f.readline().rstrip()

                if line == '':  # End of file ??
                    break

                print(linenr, line)

                if line == '-' or line.startswith(':'):  # End of message
                    proces_line(codeline, message)
                    codeline = ''

                if line == '-':  # Message Trailer
                    messages.append(message)
                    print(message)
                    message = {}

                elif codeline == 'ABNANL2A\n940\nABNANL2A':  # Message Header
                    codeline = ''
                    message = {}

                elif line.startswith(':'):
                    codeline = line

                else:
                    codeline += '\n' + line

            except Exception as err:
                print(f'Error on line {linenr}: ', err)

except FileNotFoundError:
    print(f'Cannot find file {filename}')

transactions = []

for message in messages:
    for mutation in message['mutations']:
        dd = mutation.get('boek-datum')
        transaction = OrderedDict(
            bank = message.get('bank'),
            rekeningnummer = message.get('rekeningnummer'),
            munt = message.get('begin_munt'),
            # valuta_datum_str = mutation.get('valuta-datum'),
            # boek_datum_str = mutation.get('boek-datum'),
            valuta_datum = convert_date_to_string(mutation.get('valuta-datum')),
            boek_datum = convert_date_to_string(mutation.get('boek-datum')),
            # begin_debet_credit = message.get('begin_credit_debet'),
            # beginsaldo = message.get('beginsaldo'),
            beginsaldo = convert_amount_to_string(mutation.get('beginsaldo')),
            # eind_debet_credit=message.get('eind_credit_debet'),
            # eindsaldo=message.get('eindsaldo'),
            eindsaldo = convert_amount_to_string(mutation.get('eindsaldo')),
            # credit_debet=mutation.get('transactie_credit_debet'),
            # bedrag_str = mutation.get('bedrag'],
            # bedrag=Decimal(mutation.get('bedrag').replace(',', '.')),
            bedrag = convert_amount_to_string(mutation.get('bedrag')),
            tegenrekening = mutation.get('tegenrekening', ''),
            naam = mutation.get('naam', ''),
            omschrijving=mutation.get('omschrijving', ''),
            # description = mutation.get('description', ''),
        )
        print(transaction)
        transactions.append(transaction)

filename = 'mutations.csv'
with open(filename, 'w', newline="\n", encoding='utf-8') as f:
    fieldnames = transactions[0].keys()

    writer = csv.DictWriter(f,
                            fieldnames=fieldnames,
                            dialect = 'excel',
                            delimiter=';',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            )

    writer.writeheader()
    for transaction in transactions:
        writer.writerow(transaction)
