ELIGIBLE_SALARY = 30000
ELIGIBLE_YEARS_IN_JOB = 3
salary = float(input("What do you earn per annum?"))

if salary < ELIGIBLE_SALARY:
    print("I am sorry but your salary is insufficient to apply for a loan")
else:
    yearsInTheJob = float(input("How many years have you been in your current job?"))
    if yearsInTheJob < ELIGIBLE_YEARS_IN_JOB:
        print("Sorry - your salary is sufficient "
              "but you must be over 3 years in the job")
    else:
        print("Congratulations - you may apply for a loan")
