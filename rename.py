import os
import re

path = '.'

pattern = re.compile('\ +')
replace_with = '_'

with os.scandir(path) as p:
    for entry in p:
        if not entry.name.startswith('.') and entry.is_file():
            if pattern.search(entry.name):
                new_name = pattern.sub(replace_with, entry.name)
                print(entry.name, '=>', new_name)
                os.rename(entry.name, new_name)

