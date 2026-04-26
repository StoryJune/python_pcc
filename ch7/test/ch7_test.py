#11/5/25
#Jason Li 

#Testing i/output in python

infile = open("input.txt", "r")     #r is read

lineInText = infile.readline()      #reads the first line
newStr = ""
sum = 0
while lineInText != "" :
    sum += int(lineInText)
    line = infile.readline

print(sum)

infile.close()