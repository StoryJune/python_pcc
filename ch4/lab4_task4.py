#Jason Li
#Sept 23 2025

#ch4 lab1 

#testing while loops

total = 0
validNumb = 0
flag = True

while flag:                               #while number is not negative
    numb = int(input("Enter any positive integer or a negative to stop: "))

    if numb < 0:
        flag = False
    elif numb > 0 and numb % 3 == 0:      #if number is positive and divisable by 3, add the number to the total and the validNumb for avg
        total += numb
        validNumb += 1   

if validNumb > 0:
    average = total / validNumb
    print(f"The average of the numbers divisible by three is: {average:.1f}")
else:
    print("No numbers divisible by 3 were entered.")