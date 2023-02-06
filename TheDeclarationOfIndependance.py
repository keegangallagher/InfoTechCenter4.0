# Programmer: Keegan Gallagher
# Date: 02.06.23
# Program: # Merged Welcome Screen and Gasoline Branches - Stable



"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

# Import libraries Here
import time
import sys  # Imports system Library
import random
from time import sleep

# Programmer: Keegan Gallagher
# Date: 01.23.23
# Program: InfoTech Center Upgrades

timeToSleep = 2
i = "."
x = 1

print("\n\n\033[1;35;40mWelcome - InfoTechCenter 4.0\n")
time.sleep(timeToSleep)
# print (InfoCenter 4.0 is loading
x = 0
a = 0

while x != 20:
    x += 1
    b = ("\033[1;33;40mInfoCenter 4.0 is loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\n\033[1;32;40mMission Accomplished!\n')
done = 'false'

# Programmer: Keegan gallagher
# Date: 1.30.2023
# Program: InfoTech Center 4.0 - Gasoline

"""
We will create a Function that will tell us out Fuel Gauge level
    - Create a List with Gas Levels
    - Randomize and choose from the list to determine our gas level

Create a Functon to determine our closest Gas Station
    - Create a List of gas stations
    - Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
    - PrintGas level
    - Print Closest Gas Station
"""


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()


# List of Gas Stations Function


def listOfGasStations():
    gasStations = ["shell", "Costco", "Sam's Club", "Buc-ee's", "7/11", "Speedway", "Meijer"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


# Determine Gas Level & Closest gas station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuarterTank = round(random.uniform(1, 50), 2)
    if gasLevelIndicator == "Empty":
        print("****WARNING YOU ARE ON 'EMPTY'****")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("****Warning****")
        sleep(1)
        print("Your gas tank is EXTREMELY low, checking maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("****Warning****")
        sleep(1)
        print("Your gas tank has a quarter of fuel left, the closest gas station is", listOfGasStations(),
              "which is", milesToGasStationQuarterTank, "miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full")
    else:
        print("Your tank is full")


gasLevelAlert()
