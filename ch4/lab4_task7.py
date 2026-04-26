#Jason Li
#Sept 25 2025

#ch4 lab2

str = input("Enter a string: ")
charCount = 0
digitsCount = 0
symbolCount = 0

for ch in str:
    if ch.isalpha():
        charCount += 1  
    elif ch.isdigit():
        digitsCount += 1
    else:
        symbolCount += 1

print(f"Total counts of Chars = {charCount}")
print(f"Total counts of Digits = {digitsCount}")
print(f"Total counts of Symbol = {symbolCount}")