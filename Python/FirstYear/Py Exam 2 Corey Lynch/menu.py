# Corey Lynch R00154863
#######################################################################################################################
GROUND = 10.50
BALCONY = 12.80
BOX = 15
EURO = "\u20ac"

try:
    username = str(input("Please enter your full name: "))
    username = username.capitalize()

    seat_choice = int(input("Enter seating location:\n1.Ground\n2.Balcony\n3.Box\n"))

    parking = input("Do you require a parking space?[y/n] ")
    parking = parking.lower()
    parking_req = ""

    number_of_tickets = int(input("How many tickets do you require? "))
    price = ""

    if seat_choice == 1:
        price = GROUND * number_of_tickets
        seat_name = "Ground"
    elif seat_choice == 2:
        price = BALCONY * number_of_tickets
        seat_name = "Balcony"
    elif seat_choice == 3:
        price = BOX * number_of_tickets
        seat_name = "Box"
    else:
        print("Please choose between options [1-3]. ")

    if parking == "y":
        parking_req = "Parking required."
    elif parking == "n":
        parking_req = "Parking NOT required."
    else:
        print("Please choose either: [y/n].")

    print("\n\nThank you for your booking, here are your details:\t")
    print(f"CIT Pantomime Booking Details for {username}")
    print("-----------------------------------------------------------")
    print(f"{seat_name}, {number_of_tickets} person(s), {EURO}{price}, ({parking})")

except ValueError:
    print("That is an incorrect value.")
