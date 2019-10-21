import re
from datetime import datetime, timedelta

filename = 'log.txt'

pattern = input('Geef tekst om op te filteren: ')
regex = re.compile(pattern, re.IGNORECASE + re.DOTALL)

while True:
    days = input('Geef aantal dagen om terug te gaan: ')
    if days.isdecimal():
        break
days = int(days)


with open(filename) as f:
    
    for lineno, line in enumerate(f, 1):

        if regex.search(line):

            columns = line.strip().split('\t')
            try:
                dt = datetime.strptime(columns[1], "%d-%m-%Y %H:%M:%S")
                if dt >= datetime.today() - timedelta(days=days):

                    print('%-6d %s: %s'.format(lineno, columns[1], ' || '.join(columns)))

            except:
                print(line)

