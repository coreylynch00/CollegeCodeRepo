# Corey Lynch 7/11/19

# user inputs:
family_name = input("Please enter your name: ")
weekly_energy = int(input("Please enter your energy usage per week in KWH: "))

annual_energy = weekly_energy * 52                      # calculate weekly energy consumption
annual_cost = annual_energy * 0.13                      # calculate annual energy consumption

# calculate annual savings if the family is over the national average
savings_if_consumption_reduced = annual_cost * 0.1
percent_of_national_average = (annual_energy / 4200) * 100

# display/output data:
print(f"Name: {family_name}")
print(f"Usage (kwh): {weekly_energy}")

print(f"\nReport for Household: \t{family_name.upper()}")
print(f"Annual Usage: \t\t\t{annual_energy:,} kwh")
print(f"Annual Cost: \t\t\t\u20ac{annual_cost:,.2f}")

if annual_energy > 4200:
    print(f"\nWARNING: You need to cut your usage by 10%."
          f"\nThis will save you \u20ac{savings_if_consumption_reduced:,.2f} per annum.")

else:
    print(f"Well done - you are {percent_of_national_average:.0f}% of average annual usage per household.")

