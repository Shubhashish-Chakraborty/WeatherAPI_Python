import pickle
import requests
import datetime


def getAPIkey():

    with open("./WeatherAPI_Python/API_KEY/api_key.dat", "rb") as f:

        try:
            while True:

                key = pickle.load(f)

        except EOFError:
            pass

    
    return key


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = getAPIkey()

CITY = "bhilai"

URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(URL).json()

print(response)
# print(response['name'])
# print(response['sys'])