# Wages calculator
# Author: Corey Lynch
# Date: 26/09/2019

employee_name = input('What is your name?')
hourly_rate = float(input('How much are you payed per hour?'))
hours_worked = int(input('How many hours did you work?'))

total_pay = hourly_rate * hours_worked

print(employee_name, ', your total pay this week will be £', total_pay)

