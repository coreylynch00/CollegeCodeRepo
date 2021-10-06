score1 = float(input("Exam mark #1?"))
score2 = float(input("Exam mark #2?"))
score3 = float(input("Exam mark #3?"))
average = (score1+score2+score3)/3
print("The average is " + "%0.2f"% average)

passed = average >= 40

if passed:
    print("You have passed")
else:
    print("You have failed")