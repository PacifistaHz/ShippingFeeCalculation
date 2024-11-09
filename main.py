width=input("Enter a width (cm): ")
length=input("Enter a length (cm): ")
height=input("Enter a height (cm): ")
masse=input("Enter a mass (kg): ")
distance=input("Enter a distance (km): ")
contractCustomer=input("Enter a contract customer name (Yes: 1, No: 0): ")

width=float(width)
length=float(length)
height=float(height)
masse=float(masse)
distance=float(distance)
contractCustomer=float(contractCustomer)

priceAccordingToSize=(masse*distance*5*(10**-3))+10
priceAccordingToMasse=(width*height*width*distance*5*(10**-6))+9

price=0

if priceAccordingToSize>priceAccordingToMasse:
    price=priceAccordingToSize
else:
    price=priceAccordingToMasse

if contractCustomer==1:
    price=price/2

print(price)
