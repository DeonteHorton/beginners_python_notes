import random # this is a generic import
from random import randint # this is how to import a specific function from a module
from random import (randrange, randbytes) # this is how to import multiple functions from a module
## from random import * # this is how to import all functions from a module

print("Random number between 1 and 10:", random.randint(1, 10)) # returns a random integer between 1 and 10

print("Random float:", random.random()) # returns a random float between 0 and 1

print("Random number between 50 and 100:", randint(50, 100)) # returns a random integer between 50 and 100