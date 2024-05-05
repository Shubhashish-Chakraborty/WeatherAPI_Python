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

def ConvertKelvin(kelvinValue): # camelCase

    CELSIUS = (kelvinValue - 273.15)
    FAHRENHEIT = ((kelvinValue - 273.15) * (1.8) + 32)

    return {"CELSIUS": CELSIUS , "FAHRENHEIT": FAHRENHEIT}

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = getAPIkey()

# ON PROGRESS....