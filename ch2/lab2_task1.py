#Jason Li
#Sept 3 2025
#Program used for area calculation

import math 

height = int(input("Please enter the height(in): "))
radius = int(input("Please enter the radius(in): "))
surfArea = 0

# arithmetics 
surfArea = (math.pi * radius) * (radius + (math.sqrt((pow(height, 2)) + (pow(radius, 2))))) 
# cant use ^ for power, had to include the math library

print("Here is the surface area: " , surfArea)