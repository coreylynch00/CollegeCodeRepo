# Corey Lynch 11/10/2019

fiesta = 27000
focus = 32000
kuga = 35000
golf = 36000
white = 500
black = 500
yellow = 1000
standard = 500
sport = 1500
deluxe = 2500

print("Car Options:\n")
print("\t1. Fiesta\t\u20ac27,000")
print("\t2. Focus\t\u20ac32,000")
print("\t3. Kuga\t\t\u20ac35,000")
print("\t4. Golf\t\t\u20ac36,000")
car_choice = int(input("==>"))

print("Colour Options:\n")
print("\t1. White\t\u20ac500")
print("\t2. Black\t\u20ac500")
print("\t3. Yellow\t\u20ac1,000")
colour_choice = int(input("==>"))

print("Edition:\n")
print("\t1. Standard\t\u20ac500")
print("\t2. Sport\t\u20ac1,500")
print("\t3. Deluxe\t\u20ac2,500")
edition_choice = int(input("==>"))

if car_choice == 1:
    cost_of_car = fiesta
    car = "Ford Fiesta"
elif car_choice == 2:
    cost_of_car = focus
    car = "Ford Focus"
elif car_choice == 3:
    cost_of_car = kuga
    car = "Ford Kuga"
else:
    cost_of_car = golf
    car = "VW Golf"

if colour_choice == 1:
    cost_of_colour = white
    colour = "Colour: White"
elif colour_choice == 2:
    cost_of_colour = black
    colour = "Colour: Black"
else:
    cost_of_colour = yellow
    colour = "Colour: Yellow"

if edition_choice == 1:
    cost_of_edition = standard
    edition = "Standard Edition"
elif edition_choice == 2:
    cost_of_edition = sport
    edition = "Sport Edition"
else:
    cost_of_edition = 3
    edition = "Deluxe Edition"

print("\nYour oder is:")
print(f"\t{car}\n\t{colour}\n\t{edition}\n")
print(f"\tOrder Total: \u20ac{cost_of_car + cost_of_colour + cost_of_edition:,}")

print("\nWhat is your Email Address?")
email_address = str(input("==>"))

print("\n Do you wish to apply for finance?")
print("\tYes.")
print("\tNo.")
finance_choice = str(input("==>"))

if finance_choice == "yes":
    print(f"\tWe are now emailing all relevant paperwork to {email_address}")
elif finance_choice == "no":
    print("\tPlease contact a member of our sales team to make a booking.")
else:
    print("We are having trouble with the information you provided. Choose either 'yes' or 'no'\
for finance. Alternatively, contact us on 021 432 2345")

