#Jason Li
#Sept 15 2025

#ch3 lab2 

firstInt = int(input("Enter the first integer: "))
secondInt = int(input("Enter the second integer: "))
thirdInt = int(input("Enter the third integer: "))

if firstInt == secondInt and secondInt == thirdInt:
    print("They are all the same")
elif firstInt != secondInt and secondInt != thirdInt and firstInt != thirdInt:
    print("They are all different")
else: 
    print("They are neither all the same or all different")