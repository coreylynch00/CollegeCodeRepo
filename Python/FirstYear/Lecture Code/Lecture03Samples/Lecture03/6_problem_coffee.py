# Name: problem_coffee.py
# Author:	Helen Fagan
# Description:  Cost of coffee
user_input= input('Enter the no. of coffee: ')
number_of_coffees = int(user_input)
user_input = input('Enter the cost of a coffee: ')
cost_of_coffee = float(user_input)
total_cost = number_of_coffees * cost_of_coffee
# Print a greeting to the user.
print('No. of Coffees', number_of_coffees )
print('Cost of Coffee', cost_of_coffee )
print('Total Cost ', total_cost)
