def is_pangram(stringParam):
    alphabet = "abcdefghijklnmopqrstuvwxyz"
    set1 = set(alphabet) - set(stringParam)
    if set1 == set():
        return "is a pangram"           #for true
    else:
        return "is not a pangram"       #for false
    
    