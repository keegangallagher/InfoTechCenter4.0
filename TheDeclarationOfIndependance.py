# Programmer: Keegan Gallagher
# Date: 2.8.2023
# Program: Weather System Update 

# import libraries here
import random

# Create weather condition in a list and choose it randomly
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunshine"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather() 


# VRS() to respond to the weather condition
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNWS has changed your alarm by 15 minutes because the weather forecast of:", weatherAlert)
        print("VRS has been engaged, only allowing your vehicle to go 45 MPH")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because the weather forecast of:", weatherAlert)
        print("VRS has been engaged, only allowing your vehicle to go 35 MPH")
    elif weatherAlert == "Rain":
        print("\nNWS is calling for", weatherAlert, ", please drive extra careful!")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for", weatherAlert, ", please drive extra careful!")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for", weatherAlert, ", please drive extra careful!")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your alarm by 60 minutes because the weather forecast of:", weatherAlert)
        print("VRS has been engaged, only allowing your vehicle to go 25 MPH")
    else:
        print("\nNWS is calling for", weatherAlert, ", please drive safely despite these conditions.")


vehicleResponseSystem()