#Jason Li
#Sept 10 2025

str_input = input("Please enter your string: ")
str_length = len(str_input)

firstMiddle = (str_length // 2) - 1
secondMiddle = str_length // 2

str_input = str_input[:firstMiddle] + str_input[secondMiddle] + str_input[firstMiddle] + str_input[secondMiddle+1:]

print(f"New string: {str_input}")