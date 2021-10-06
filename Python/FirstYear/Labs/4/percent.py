# Author: Corey Lynch 2/10/2019

from_cork = int(input("How many are people are from Cork?"))
not_from_cork = int(input("How many people are not from Cork?"))
total_in_class = int(from_cork + not_from_cork)

percent_from_cork = float(from_cork / (from_cork + not_from_cork)) * 100

print("\t")
print(f"The total number of students in the class is {total_in_class}")
print(f"The percent from Cork is {percent_from_cork:.1f}%")
