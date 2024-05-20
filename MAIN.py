import pickle
import requests
# import datetime
import os
import time
import pygetindia as pyin

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



def TEMPERATURE_MAIN(CITY):

    print()


    URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(URL).json()

    # print(ConvertKelvin(response['main']['temp'])['CELSIUS'])

    print(f"Temperature({CITY}) : {ConvertKelvin(response['main']['temp'])['CELSIUS']} °C")





    print()



def select_state_city():
    
    print()


    statesList = pyin.states()

    for state in range(len(statesList)):

        print(f"{state + 1} -> {statesList[state]}")


    print("< Select State >")
    

    print()

    getStateNum = input("Enter State Number : ")

    # Selecting State

    for num in range(len(statesList)):

        if (int(getStateNum) == (num + 1)):

            State_Selected = statesList[num]
    

    StatesCitiesDICT = pyin.states_cities()

    # Selecting the respective cities for the selected State


    for key in StatesCitiesDICT:

        if (State_Selected == key):

            RESP_Cities_List = StatesCitiesDICT[key]


    # Displaying the cities
    
    for city in range(len(RESP_Cities_List)):

        print(f"{city + 1} -> {RESP_Cities_List[city]}")

    getCityNum = input("Enter City Number : ")


    # Selected the CITY!!

    for num in range(len(RESP_Cities_List)):

        if (int(getCityNum) == (num + 1)):
            City_Selected = RESP_Cities_List[num]


    TEMPERATURE_MAIN(City_Selected) # Main temperature function invoked!!




while (True):

    options = ["1-> Select State and City and get Temperature" , "2-> EXIT\n"]


    optList = []

    for opt in range(len(options)):

        to_append = opt + 1
        optList.append(to_append)
        print(options[opt])


    getChoice = input(f"Enter Your Choice {optList} : ")
    

    if (getChoice.isdigit()):

        if (int(getChoice) == 1):

            select_state_city()
        
        
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