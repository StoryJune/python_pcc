#Jason Li
#Sept 25 2025

#ch4 lab2

#while loops with power and square 

#start at 2 
numb1 = 2 #for first question
numb2 = 1 #for second question
numb3 = 2 #for third question

total1 = 0
total2 = 0

#need a check for even numbers 
evenNumb = True        #first set to true because our number starts at 2

#Edge chase check
if numb1 % 2 == 0:      #if number is even
    evenNumb = True    #even = true
else:
    evenNumb = False   #not even = false

while numb1 <= 100 and evenNumb: 
    total1 += numb1                                  #add total by numb
    numb1 += 2                                       #increment number by 2
    #print(f"Debug: total {total} numb1 {numb}")

print(f"Sum of even numbers between 2 and 100: {total1}")

while numb2 <= 100:
    powNumb = numb2 ** 2                             #initialize number as powered   
    total2 += powNumb                                #repeat the previous from above while loop
    numb2 += 1
    #print(f"Debug: total {total2} numb2 {numb2} powerNumb {powNumb}")

print(f"Sum of squares between 1 and 100: {total2}")

print(f"Power of 2 from 20 up to 30: ", end = " ")   
power = 20
while power <= 30:
    powNumb = numb3 ** power                         #initialize number as powered                                       
    print(powNumb, end = " ")                        #but now we increment the power too
    power += 1                                             
    #print(f"Debug: numb3 {numb3} powerNumb {powNumb} power {power}")
