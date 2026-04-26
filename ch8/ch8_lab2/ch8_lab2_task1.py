#11/3/25
#Jason Li 

#Set properties

from unique import is_unique
from pangram import is_pangram

def main():
    string1 = "Python"
    string2 = "Java"

    string3 = "Mary had a little lamb"
    string4 = "The quick brown fox jumps over the lazy dog"

    string5 = "Mammon"

    print(f"{string1}: {is_unique(string1)}")
    print(f"{string2}: {is_unique(string2)}")
    print(f"{string3}: {is_pangram(string3)}")
    print(f"{string4}: {is_pangram(string4)}")
    print(f"{string5}: {is_unique(string5)}")

main()