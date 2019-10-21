import urllib.request
import json

city = input('Give city: ')

# openwheathermap.org current weather api
url  = 'http://api.openweathermap.org/data/2.5/weather'
url += '?appid=d1526a9039658a6f76950cff21823aff'
url += '&units=metric'
url += '&mode=json'
url += '&q=' + city

print(url)

site = urllib.request.urlopen(url)
response = str(site.read(), encoding='utf-8')

print(response)

r = json.loads(response)

print(r)

description = r['weather'][0]['description']
temperature = r['main']['temp']

print('Weather in %s: %s, temperature %.0f°C' % (city, description, temperature))
