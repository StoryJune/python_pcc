#Jason Li
#Sept 17 2025

#ch3 lab3 

#demo program

#string & substring from user input
str = input("Enter a string: ")
subStr = input("Enter a substring: ")

if subStr in str: #check for substring
    print("The string does contain the substring.")

    strCount = str.count(subStr)
    print("It contains", strCount, "instance(s)")

    charPos = str.find(subStr)
    print("The first occurence starts at position", charPos)

    if str.startswith(subStr):
        print("The string starts with the substring.")
    else: 
        print("The string doesn't start with the substring.")
    
    if str.endswith(subStr):
        print("The string ends with the substring.")
    else: 
        print("The string doesn't end with the substring.")

else: 
    print("The string doesn't contain the substring.")
