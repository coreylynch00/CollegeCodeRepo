string = input("Please type a word/phrase >>> ")

number_of_characters = len(string)
for k in range (number_of_characters):
    print(string[k], end="*")


print()
print()

# looping without a counter
for character in string:
    print(character, end='*')

print()
print()

# Must go down as far as but not including -1
for k in range(number_of_characters - 1, -1, -1):
    print(string[k], end="*")

