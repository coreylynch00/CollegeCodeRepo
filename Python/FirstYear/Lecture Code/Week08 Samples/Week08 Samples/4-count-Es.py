string = input("Please type a word/phrase >>> ")
count_es = 0

for character in string:
    if character.lower() == 'e':
        count_es += 1

print("There are", count_es, "e's in the word/phrase")