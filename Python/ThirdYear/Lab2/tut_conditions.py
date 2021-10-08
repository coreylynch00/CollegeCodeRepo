# LAB 2
salary = int(input("Enter your salary in form [000000]  >>> "))
child = input("Do you have 1 or more children [y/n]  >>> ")

# if sal > 70 - tax 55 - regardless

# if sal >= 50 but sal < 70 - tax 50 NO KID
# if sal >= 50 but sal < 70 - tax 45 WITH KID

# if sal >= 30 but sal < 50 - tax 40 NO KID
# if sal > 30 but sal < 50 - tax 35 WITH KID

# if sal < 30 - tax 30 - regardless

if salary >= 70000:
    tax = salary * 0.55
    take_home = salary - tax
    print(f"Tax: €{tax:.2f}, Takehome: €{take_home:.2f}")

elif 50000 <= salary < 700000 and child == 'n':
    tax = salary * 0.5
    take_home = salary - tax
    print(f"Tax: €{tax:.2f}, Takehome: €{take_home:.2f}")

elif 50000 <= salary < 700000 and child == 'y':
    tax = salary * 0.45
    take_home = salary - tax
    print(f"Tax: €{tax:.2f}, Takehome: €{take_home:.2f}")

elif 30000 <= salary < 50000 and child == 'n':
    tax = salary * 0.4
    take_home = salary - tax
    print(f"Tax: €{tax:.2f}, Takehome: €{take_home:.2f}")

elif 30000 <= salary < 50000 and child == 'y':
    tax = salary * 0.35
    take_home = salary - tax
    print(f"Tax: €{tax:.2f}, Takehome: €{take_home:.2f}")

else:
    tax = salary * 0.3
    take_home = salary - tax
    print(f"Tax: €{tax:.2f}, Takehome: €{take_home:.2f}")
