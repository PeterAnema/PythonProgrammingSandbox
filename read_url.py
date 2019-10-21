import urllib.request
import re

url = 'http://' + input('Geef site URL: ')

response = urllib.request.urlopen(url)
html = str(response.read())

regex = re.compile(r'<a href=[\"\']?(\S*\.\S*)[\"\']?.*?>')

results = regex.findall(html)

if results:
    print("results")
    for r in results:
        print(r)
else:
    print("no results")


