# anything received from the command line is always a string
name = input("What is your name? ") # gets the user's name from the command line

int_number = int("3") # casts a string to an integer
float_number = float("3.14") # casts a string to a float
string = str(3) # casts an integer to a string

rounded_number = round(float_number, 2) # rounds a float to the nearest integer, the second argument is how many decimal places to round to


ex_numbers = "123456789" # how to set a variable
print(ex_numbers[3]) # gets the 4th character in the string

print(ex_numbers[0:3]) # how to print a slice of a string
print(ex_numbers[3:]) # gets the 3rd character to the end of the string
print(ex_numbers[:6]) # gets the beginning of the string to the 6th character

print("Hello world! \nWe made a new line!") #gets the string to print on a new line
print("Hello world! \tWe got tabbed! :]") #gets the string to print with a tab... 4 spaces

print("Hello world! \rHow are you?") #gets the string to print with a carriage return... goes back to the beginning of the line

# creates a function that prints hello world... inside function, must be 4 spaces over for python to know it's part of the function
def print_hello_world():
    print("Hello world!")

print_hello_world() # calls the function to print hello world
