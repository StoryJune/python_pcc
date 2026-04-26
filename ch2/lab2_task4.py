#Jason Li
#Sept 10 2025

#Demonstrating string/int format

phoneNumb = input("Please enter your unformatted phone number: ")
print(f"The phone number is: {phoneNumb}") 

#String splicing 
areaCode = phoneNumb[0:3]
threeDigits = phoneNumb[3:6]
extension = phoneNumb[6:]

print(f"The formatted number is: ({areaCode}) {threeDigits}-{extension}")