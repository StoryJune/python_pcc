#Jason Li
#Sept 3 2025
#A program that demonstrates the different type of data 

a = int(input("Please enter the first integer: ")) # takes in user input for the first integer
b = int(input("Please enter the second integer: ")) # takes in user input for the second integer

print("You entered:", a, "and", b) 

sum = a + b
print("Sum: " , sum)

diff = (a - b)
print("Diff: " , diff)

prod = a * b 
print("Product: " , prod)

avg = (a + b) / 2 
print("Average: " , avg)

dist = abs(diff) # python's built in functions
print("Distance: " , dist)

minNumb = min(a, b) # python's built in functions
print("Minimum: " , minNumb)

maxNumb = max(a , b) # python's built in functions
print("Maximum: " , maxNumb)