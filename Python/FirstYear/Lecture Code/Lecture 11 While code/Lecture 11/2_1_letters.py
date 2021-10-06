str = input("Please type a word/phrase >>> ")
numberOfChars = len(str)
i = 0
while i < numberOfChars:
    print(str[i], end="*")
    i += 1