#Jason Li
#Sept 17 2025

#ch3 lab3 

strInput = input("Enter any string: ")


if strInput.isalpha(): #check for all letters
    print("all letters") 
elif strInput.isdigit(): #check for all letters
    print("all digits")
elif strInput.isalnum(): #check for string
    print("letters and digit")
else:
    print("mix of all")