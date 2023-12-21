print("Hello! Welcome to the Rectangular Prism Volume Calculator!")
print("Please enter the length, width, and height of your rectangular prism below.")
l = input("Length: ")
w = input("Width: ")
h = input("Height: ")

def volume_calc(l=5, w=5, h=5):
    return int(l) * int(w) * int(h)


volume = str(volume_calc(l, w, h))

print("The volume of your rectangular prism is " + volume + " cubic units.")