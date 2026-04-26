#Jason Li
#Sept 7 2025
#Program to demonstrate string methods and string repetition

#Given a string, do the following:
#Print the length of the string
#Replace all lower case ‘a’ with upper case ‘A’ and print it
#Capitalize the whole string and print it.
#Print the second character
#Print the last character
#Print the middle character

str_mesg = input("Please enter your string: ")
str_leng = len(str_mesg)

print("The length of the string is: ", str_leng) # prints string length

print("The replaced string is: ", str_mesg.replace("a", "A")) # replaces lowercase 'a' with 'A'

print("The capitalized string is: ", str_mesg.upper()) # using upper() to convert the string
 
print("The second character is: ", str_mesg[1]) # searching thru an char array

print("The last character is: ", str_mesg[str_leng - 1]) # searching from the last of the array

print("The middle character is: ", str_mesg[str_leng // 2]) # searching from the middle by looking for the modulo