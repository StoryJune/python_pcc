#Jason Li
#Sept 25 2025

#ch4 lab2

#program for vowels

#we need to initialize vowels (a, e, i, o, u)
vowelStr = input("Enter a string: ")                #ask for string that we're comparing
vowels = "aeiouAEIOU"                               #container for vowel
vowelCount = 0                                      #tracks count of vowels
index = 0                                           #condition
strLeng = len(vowelStr)

#while index < strLeng:                              #while we having reach the end of the string, 
#    if vowelStr[index] in vowels:                   #if any vowels are present based on the index
#        vowelCount += 1                             #increment vowel count
#    index += 1                                      #increment index to search through the string

    
for char in vowelStr:
        if char in vowels:
                vowelCount += 1

print(f"The string has {vowelCount} vowel.")