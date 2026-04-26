#Jason Li
#Sept 3 2025
#Program used for area calculation

#Giving change. Implement a program that directs a cashier on how to give change. 
#The program has two inputs: the amount due and the amount received from the customer. 
#Display the dollars, quarters, dimes, nickels, and pennies that the customer should receive in return. 
#In order to avoid roundoff errors, the program user should supply both amounts in pennies, for example, 274 instead of 2.74.

# default initializations
amountDue = float(input("Please enter the amount due: "))
amountReceived = float(input("Please enter the amount received: "))

# dollar system
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

# dollar values
dollarVal = 100
quarterVal = 25
dimeVal = 10
nickelVal = 5
pennyVal = 1

# arithmetic for change
giveChange = amountReceived - amountDue # 693 - 411 = 282

print("The change is: ")
dollars = giveChange // dollarVal # 282 // 100 = 2.82 -> 2
print(dollars, "dollars")

quarters = (giveChange % dollarVal) // quarterVal #  1. 282 % 100 = 82 
print(quarters, "quarters")                       #  2. 82 // 25 = 3 

dimes = ((giveChange % dollarVal) % quarterVal) // dimeVal # 1. 282 % 100 = 82  
print(dimes, "dimes")                                       # 2. 82 % 25 = 7 
                                                            # 3. 7 // 10 = 0 

nickels = ((giveChange % dollarVal) % quarterVal % dimeVal) // nickelVal # 1. 282 % 100 = 82  
print(nickels, "nickels")                                                # 2. 82 % 25 = 7
                                                                         # 3. 7 % 10 = 0.7 -> 7
                                                                         # 4. 7 // 5 = 1

pennies = ((((giveChange % dollarVal) % quarterVal) % dimeVal) % nickelVal) // pennyVal # 1. 282 % 100 = 82  
print(pennies, "pennies")                                                               # 2. 82 % 25 = 7 
                                                                                        # 3. 7 % 10 = 7
                                                                                        # 4. 7 % 5 = 2 
                                                                                        # 5. 2 // 1 = 2 