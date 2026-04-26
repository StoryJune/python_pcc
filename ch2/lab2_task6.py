#Jason Li
#Sept 10 2025

#Program to calculate a car's price

#User inputs
carPrice = int(input("Enter the cost of the car: "))
milesPerYear = int(input("How many miles will you drive each year? "))
pricePerGallon = int(input("Enter the price of gas per gallon: "))
milesPerGallon = int(input("Enter the fuel efficiency in MPG: "))
depreciateCost = int(input("How much can you sell the car for after 5 years? "))

totalGasCost = ((milesPerYear/milesPerGallon) * pricePerGallon) * 5
totalCost = carPrice + totalGasCost - depreciateCost

print(f"The total cost of ownership is {totalCost:.2f}")