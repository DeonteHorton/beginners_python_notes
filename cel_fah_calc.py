print("Welcome user to the Celsius to Fahrenheit calculator! \nPlease enter the temperature in Celsius below.")
celsius = input("Temperature in Celsius: ")

def cel_fah_calc(celsius=10):
    return round((int(celsius) * 1.8) + 32, 1) # rounds to the nearest tenth

fahrenheit = str(cel_fah_calc(celsius)) # converts the float to a string since print can only print strings

print("It is " + fahrenheit + " degrees Fahrenheit.")