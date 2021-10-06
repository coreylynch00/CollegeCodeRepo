ELIGIBLE_SALARY = 30000
ELIGIBLE_YEARS_IN_JOB = 3
salary = float(input("What do you earn per annum?"))
if salary < ELIGIBLE_SALARY:
    print("I am sorry but your salary is insufficient to apply for a loan")
else:
    yearsInTheJob = float(input("How many years have you been in your current job?"))

if yearsInTheJob < ELIGIBLE_YEARS_IN_JOB:
    print("\n\nSorry - your salary is sufficient but you must be in the job over 2 years to be eligible")
    print("We have emailed a copy of your application to calum.obrien@mtcit.ie")
else:
    print("Congratulations -you may apply for a loan")
