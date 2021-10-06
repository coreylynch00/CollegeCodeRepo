# Corey Lynch 7/11/19

name = input("Enter your name.")

number_of_characters = len(name)
for x in range(number_of_characters - 1, -1, -1):
    print(name[x], end="")
