# Programmer: Keegan Gallagher
# Date: 01.23.23
# Program: InfoTech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

#Import libraries Here
import time
import sys # Imports system Library

timeToSleep = 2
i = "."
x = 1

print("\n\nWelcome - InfoTechCenter 4.0")
time.sleep(timeToSleep)
#print (InfoCenter 4.0 is loading
x = 0
a =0

while x != 20:
    x += 1
    b = ("\033[1;33;40m InfoCeter 4.0 is loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Done!')