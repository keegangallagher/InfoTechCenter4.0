# Programmer: Keegan Gallagher
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
import random


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Running on Fumes",'low',"Halfway there","alllll good","Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


print(gasLevelGauge())


