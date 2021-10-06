# Corey Lynch 14/10/2019

user_name = str(input("Enter your name."))

if user_name.capitalize() == "John" \
    or user_name.capitalize() == "George" \
    or user_name.capitalize() == "Ringo" \
   or user_name.capitalize() == "Paul":
    print("Hey, that's the name of a Beatle!")
else:
    print("That's a nice name!")
