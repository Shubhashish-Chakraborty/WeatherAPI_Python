import pickle
import requests
import datetime
import os
import time

print()
os.system("cls")

print("*"*60)

print("Welcome to the Weather App, Made by Shubhashish Chakraborty!")

print("*"*60 , '\n')



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

#Main Menu Drive For the APP


def getTemperature():
    
    print()

    # WORK FROM HERE...

    print()







while (True):

    options = ["1-> Find Temperature" , "2-> EXIT\n"]


    optList = []

    for opt in range(len(options)):

        to_append = opt + 1
        optList.append(to_append)
        print(options[opt])


    getChoice = input(f"Enter Your Choice {optList} : ")
    

    if (getChoice.isdigit()):

        if (int(getChoice) == 1):

            getTemperature()
        
        
        elif (int(getChoice) == 2): #EXIT

            print("Program closed successfully!")
            time.sleep(1)
            # os.system('cls')
            break

        else:

            os.system("cls")
            print("Invalid Input, Try Again!")
            


    else:

        os.system("cls")
        print("Invalid Input, Try Again!")