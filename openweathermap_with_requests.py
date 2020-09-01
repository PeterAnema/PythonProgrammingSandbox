import requests
import json

city = input("Give city: ")

# openwheathermap api
url  = "http://api.openweathermap.org/data/2.5/weather"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&q=" + city

print(url)

try:
    response = requests.get(url)

except Exception as err:
    print("Cannot connect to " + url)
    print(err)

else:
    print(response.text)

    if (response.status_code == 200):

        body = response.text

        print(response.status_code)
        print(body)

        decoded = response.json()

        temperature = decoded['main']['temp']
        description = decoded['weather'][0]['description']

        print(f'Weather in {city} is {description}. Temperatuur is {temperature}.')

    elif response.status_code == 404:
        print("%s not found" % (city))

    else:
        print("error for city %s" % (city))


