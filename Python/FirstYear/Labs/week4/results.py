# Author: Corey Lynch 2/10/2019

math_result = int(input("What was your Math result?"))
science_result = int(input("What was your Science result?"))
english_result = int(input("What was your english result?"))

total_grade = (math_result + science_result + english_result) / 3

print("\t")

if total_grade > 50:
    print(f"Congrats! You've passed! Your final grade was {total_grade:.0f}%")
elif total_grade < 39:
    print(f"You have failed! Wake up! Your final grade was {total_grade:.0f}%")
else:
    print(f"You passed by the skin of your teeth! Your grade was {total_grade:.0f}%")