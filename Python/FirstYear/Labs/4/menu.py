# Corey Lynch 10/10/2019

cheeseburger = 2.45
hamburger = 2.35
chickenburger = 3.65
smallchips = 2.90
largechips = 3.50
currychips = 3.85
coke = 1.25
fanta = 1.25
milk = 1.50

print(f"Burger Menu")
print(f"\t1. Cheeseburger \u20ac2.45")
print(f"\t2. Hamburger \u20ac2.35")
print(f"\t3. Chicken Burger \u20ac3.65 \n")
burger_choice = int(input("==> "))
print(f"Chips Menu")
print(f"\t1. Small \u20ac2.90")
print(f"\t2. Large \u20ac3.50")
print(f"\t3. Curry \u20ac3.85 \n")
chips_choice = int(input("==>"))
print(f"Drinks Menu")
print(f"\t1. Coke \u20ac1.25")
print(f"\t2. Fanta \u20ac1.25")
print(f"\t3. Milk \u20ac1.50")
drink_choice = int(input("==>"))

if burger_choice == 1:
    cost_of_burger = cheeseburger
elif burger_choice == 2:
    cost_of_burger = hamburger
else:
    cost_of_burger = chickenburger

if chips_choice == 1:
    cost_of_chips = smallchips
elif chips_choice == 2:
    cost_of_chips = largechips
else:
    cost_of_chips = currychips

if drink_choice == 1:
    cost_of_drink = coke
elif drink_choice == 2:
    cost_of_drink = fanta
else:
    cost_of_drink = milk

print(f"The total cost is \u20ac{cost_of_burger + cost_of_chips + cost_of_drink:.2f}")
