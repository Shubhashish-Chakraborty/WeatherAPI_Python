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


def ConvertTemp(KelvinValue):

    CELSIUS = (KelvinValue - 273.15)
    FAHRENHEIT = ((KelvinValue - 273.15) * (1.8) + 32)

    return {"CELSIUS": CELSIUS , "FAHRENHEIT": FAHRENHEIT}


CITY = "Bhilai"


URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(URL).json()

temp_kelvin = response['main']['temp']

print(ConvertTemp(temp_kelvin))