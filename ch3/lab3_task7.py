#Jason Li
#Sept 15 2025

#ch3 lab2 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
annual_Income = float(input("Enter your income: "))
has_good_credit = False

if age >= 18:
    if annual_Income >= 30000:
        has_good_credit = True
    else:
        print("Annual income does not meet required minimum")
else: 
    print("Not able to take out the loan due to age restrictions")

if has_good_credit == True:
    print("You qualify for the loan.")
else: 
    print("You do not qualify for the loan.")