str = input("Please type a word/phrase >>> ")
numberOfChars = len(str)
i = 0
letters = 0
while i < numberOfChars:
    if str[i].isalpha():
        letters += 1
    i += 1

print("There are", letters , "letters in the word/phrase")