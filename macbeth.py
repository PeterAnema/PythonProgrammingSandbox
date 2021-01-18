import re
import sys

import xml.etree.ElementTree as ET

# Load an XML document and get the root element
tree = ET.parse(r'Macbeth.xml')
root = tree.getroot()

# for e1 in root:
#     print(e1.tag)
#     for e2 in e1:
#         print('   ', e2.tag)
#         for e3 in e2:
#             print('       ', e3.tag)

print('\n------ PLAY TITLE -------------------------------------\n')

title = root.find('TITLE')
print(title.text)

print('\n------ PERSONAE -------------------------------------\n')

persona = root.iter('PERSONA')
for p in persona: 
    print(p.text)

print('\n------ SCENES -------------------------------------\n')

scenes = root.findall('.//SCENE/TITLE')
for s in scenes:
    print(s.text)

sys.exit()

print('\n------ SPEECHES BY DUNCAN -------------------------\n')

speeches = root.findall('.//SPEECH[SPEAKER="DUNCAN"]')
for s in speeches:
    for l in s.findall('LINE'):
        print(l.text)
    print()

print('\n------ SPEECH WITH MOST LINES ---------------------\n')
    
speeches = root.findall('.//SPEECH')

max_length = max([len(speech.findall('LINE')) for speech in speeches])

for scene in root.findall('.//SCENE'):
    for speech in scene.findall('.//SPEECH'):
        if len(speech.findall('LINE')) == max_length:
            print(scene.find('TITLE').text)
            print(speech.find('SPEAKER').text)
            for l in speech.findall('LINE'):
                  print(l.text)
            print()

print('\n------ ALL LINES WITH WORD CASTLE -----------------\n')

for l in root.iter('LINE'):
    if l.text and 'castle' in l.text.lower():
        print(l.text)
