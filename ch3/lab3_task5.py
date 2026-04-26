#Jason Li
#Sept 15 2025

#ch3 lab2 

#program to calculate shipping cost 

#grabbing user input

isInternational = input("Are you shipping internationally (yes or no)? ")
isState = False
shipping_rate = 0

if isInternational.lower() == "yes":
    shipping_rate = 10 
else: 
    isState = input("Are you shipping continential (yes or no)? ")
    if isState.lower() == "yes":
        shipping_rate = 5
    else:
        shipping_rate = 10

print(f"The shipping rate is ${shipping_rate:.2f}")