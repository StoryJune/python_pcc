#Jason Li
#Sept 18 2025

#ch3 lab3 

#analyze the string and use methods taught in class
str = "   Hello, World   "

#print string for better visuals
print(f"The string we're viewing: {str}")

#count the letter l
print(f"The numbers of l's is: {str.count('l')}")

#replace the excesses space with * 
print(str.replace('   ', '***'))

#replaces space on right 
updStrOne = str.lstrip('   ')
print("***" + updStrOne + "***")

#replaces space on left
updStrTwo = str.rstrip('   ')
print("***" + updStrTwo + "***")

#strip and then replace spaces
updStrThree = str.strip('   ')
print(updStrThree.replace('o', '***'))