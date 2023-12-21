from random import randint

car = input("What kind of car do you drive or would like to drive? ")

gas_tank_holds = randint(10, 25)
mile_before_refuel = randint(200, 400)

def miles_per_gallon(car="VolksWagon"):
    mpg = mile_before_refuel // gas_tank_holds # the double // means floor division, meaning it rounds down to the nearest integer
    if mpg < 20:
        return "Your '" + car + "' is a gas guzzler!" + " You can only get " + str(mpg) + " miles per gallon before refueling close to empty on a tank that holds " + str(gas_tank_holds) + " gallons!"
    else:
        return "Your '" + car + "' is fuel efficient! You can get " + str(mpg) + " miles per gallon! You can get " + str(mpg) + " miles per gallon before refueling close to empty on a tank that holds " + str(gas_tank_holds) + " gallons!"

print(miles_per_gallon(car))