str = input("Please type a word/phrase >>> ")
numberOfChars = len(str)
i = 0
count = 0
while i < numberOfChars:
    if str[i]== "e" or str[i] == "E":
        count += 1
    i += 1

print("There are", count , "e's in the word/phrase")