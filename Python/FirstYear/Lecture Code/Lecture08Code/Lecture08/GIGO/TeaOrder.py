# Demonstrate GIGO
# try:
#     COST_OF_COFFEE = 2.35
#     number_of_people = int(input("Number of people? "))
#     total_cost = COST_OF_COFFEE * number_of_people
#     print("Total cost = €{:.2f}".format(total_cost))
# except ValueError:
#     print("Only whole numbers please!")











# Fix GIGO
try:
    COST_OF_COFFEE = 2.35
    number_of_people = int(input("Number of people? "))

    if number_of_people < 0:
        print("Number of people cannot be negative")
    elif number_of_people == 0:
        print("So there are no people? Ok!")
    else:
        total_cost = COST_OF_COFFEE * number_of_people
        print("Total cost = €{:.2f}".format(total_cost))
except ValueError:
    print("Only whole numbers please!")


