#Jason Li
#Sept 23 2025

#ch4 lab1 

#testing while loops

total = 0 
average = 0
scoreCount = 0 
failCount = 0 
passCount = 0


grade = int(input("Enter a grade or -1 to finish: "))

if grade > 0:           #if our grades is not empty, then set max and min to the first score
    maxScore = grade
    minScore = grade

while grade > 0:        #while grades is not empty
    total += grade      #(total = total + grade (to get the sum))

    if grade >= 60:     #if grades are passing +1 to pass, if not failing +1
        passCount += 1
    else:
        failCount += 1

    scoreCount += 1     #increment the score after every evaluation

    if grade > maxScore: #if the current score is great than the maxscore, than the current score is the maxscore
        maxScore = grade
    if grade < minScore: #if the current score is less than the maxscore, than the current score is the maxscore
        minScore = grade

    grade = int(input("Enter a grade or -1 to finish: "))   #prime read

average = total/scoreCount  #finding average

print(f"The average grade is {average:.2f}")
print(f"Number of passing grades is {passCount}")
print(f"Number of failing grades is {failCount}")
print(f"The maximum grade is {maxScore:.2f}")
print(F"The minimum grade is {minScore:.2f}")