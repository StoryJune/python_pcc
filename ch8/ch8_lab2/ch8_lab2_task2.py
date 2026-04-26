#11/3/25
#Jason Li 

#Dictionary


def charCount(string):
    countSet = {}
    for ch in string:
        if ch not in countSet:
            countSet[ch] = 1 
        else:
            countSet[ch] += 1
    return countSet

def main():
    theString = "mississipi"
    charCountTotal = charCount(theString)
    print("The number of times each letter occurs in the string \"" + theString + "\":")
    for ch in charCountTotal:
        print(ch, " ", charCountTotal[ch], end="")
        print()

main()