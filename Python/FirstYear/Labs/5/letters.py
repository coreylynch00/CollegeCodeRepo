# Corey Lynch 14/10/2019

try:
    letter = str(input("Enter a letter."))
    if letter.isalpha():
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            print("That is a vowel.")
        elif letter == "y":
            print("Sometimes this can be a vowel. For example in the word 'rhythm'. Otherwise a constant")
        else:
            print("That is a constant.")
    else:
        raise ValueError

except ValueError:
    print("You must enter a letter!")
