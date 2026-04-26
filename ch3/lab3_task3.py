#Jason Li
#Sept 11 2025

#input
firstWord = input("Enter the first word in a compound word: ")
secondWord = input("Enter the second word in a compound word: ")
#condition
wordLength = len(firstWord + secondWord)
#statement
if wordLength % 2 == 0:
    print(f"{firstWord}{secondWord}")
else: 
    print(f"{firstWord}-{secondWord}")