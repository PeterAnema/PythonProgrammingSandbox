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
    r = requests.get(url)

except Exception as err:
    print("Cannot connect to " + url)
    print(err)

else:
    print(r.text)

    if (r.status_code == 200):
        responseDict = json.loads(r.text)
        temperature = responseDict["main"]["temp"]
        print("Temparture in %s is %.0f°" % (city, temperature))

    elif (r.status_code == 404):
        print("%s not found" % (city))

    else:
        print("error for city %s" % (city))
