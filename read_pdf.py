import re

# first install PyPDF2 wiyh pip install PyPDF2
# importing all the required modules
import PyPDF2

# creating an object
file = open('example.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(pdfReader.numPages)

pages = dict()
for pagenr in range(pdfReader.numPages):
    page = pdfReader.getPage(pagenr)
    pages[pagenr] = page.extractText()

# for pagenr, page in pages.items():
#     print('page %d' % pagenr, 80 * '-')
#     print(page)

text_to_find = 'Speech'
re_pattern = re.compile(r'^(.*?' + text_to_find + '.*?)$', re.MULTILINE)

for pagenr, page in pages.items():
    matches = re_pattern.search(page)
    if matches:
        n = len(matches.groups())
        print('Found the pattern %d times on page nr %d' % (n, pagenr))
        for match_group in matches.groups():
            print(match_group)
