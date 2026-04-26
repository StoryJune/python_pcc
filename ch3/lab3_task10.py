#Jason Li
#Sept 18 2025

#ch3 lab3 

month = int(input("Enter your month as a number: "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12: #any odd month
        print("There are 31 days")
    case 4 | 6 | 9 | 11:
        print("There are 30 days")
    case 2: #any even month
        print("There are 28 or 29 days")
    case _: # _ underscore means if there are no other matches
        print("Invalid month")